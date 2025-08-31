import pygame
from pygame.locals import *
from entities.player import Player

def main():
    # Initialize pygame first
    pygame.init()
    
    # Define fps
    clock = pygame.time.Clock()
    fps = 50

    screenWidth = 600
    screenHeight = 800

    screen = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption('Galaxy Shooter')

    # Background Image
    bg = pygame.image.load('assets/images/background2.png')

    bg_x = 0
    bg_y = 0

    def draw_bg():
        screen.blit(bg, (bg_x, bg_y))

    # Create player
    player = Player(screenWidth // 2, screenHeight - 130, screenWidth)
    
    # Create sprite groups
    player_group = pygame.sprite.Group()
    player_group.add(player)
    
    bullet_group = pygame.sprite.Group()

    run = True
    while run:
        clock.tick(fps)
        draw_bg()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = player.shoot()
                    if bullet:
                        bullet_group.add(bullet)

        # Update sprites
        player_group.update()
        bullet_group.update()
        
        # Draw sprites
        player_group.draw(screen)
        bullet_group.draw(screen)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
