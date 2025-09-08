import pygame

class Alien_Bullets(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("img/alien_bullet.png")
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]

	def update(self):
		self.rect.y += 2
		if self.rect.top > self.screen_height:
			self.kill()
		if pygame.sprite.spritecollide(self, self.spaceship_group, False, pygame.sprite.collide_mask):
			self.kill()
			