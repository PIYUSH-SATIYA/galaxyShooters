import pygame
import random
from pygame.locals import *
from entities.player import Player
from entities.enemy import Enemy
from entities.explosion import Explosion

def main():
    pygame.init()

    clock = pygame.time.Clock()
    fps = 50

    screenWidth = 600
    screenHeight = 800

    screen = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption('Galaxy Shooter')

    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 36)

    bg = pygame.image.load('assets/images/background2.png')

    bg_x = 0
    bg_y = 0

    def draw_bg():
        screen.blit(bg, (bg_x, bg_y))

    game_over = False
    game_over_timer = 0
    game_over_delay = 3000  

    player = Player(screenWidth // 2, screenHeight - 130, screenWidth)
    
    player_group = pygame.sprite.Group()
    player_group.add(player)
    
    bullet_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    enemy_bullet_group = pygame.sprite.Group()
    explosion_group = pygame.sprite.Group()
    
    for i in range(5):
        enemy = Enemy(100 + i * 80, 100, screenWidth)
        enemy_group.add(enemy)

    def reset_game():
        """Reset the game to initial state"""
        nonlocal game_over, game_over_timer
        game_over = False
        game_over_timer = 0
        
        bullet_group.empty()
        enemy_group.empty()
        enemy_bullet_group.empty()
        explosion_group.empty()
        player_group.empty()
        
        new_player = Player(screenWidth // 2, screenHeight - 130, screenWidth)
        player_group.add(new_player)
        
        for i in range(5):
            enemy = Enemy(100 + i * 80, 100, screenWidth)
            enemy_group.add(enemy)
        
        return new_player

    def draw_game_over():
        """Draw game over screen"""
        overlay = pygame.Surface((screenWidth, screenHeight))
        overlay.set_alpha(128)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))
        
        game_over_text = font.render("GAME OVER", True, (255, 0, 0))
        game_over_rect = game_over_text.get_rect(center=(screenWidth // 2, screenHeight // 2 - 50))
        screen.blit(game_over_text, game_over_rect)
        
        if game_over_timer > game_over_delay:
            restart_text = small_font.render("Press R to Restart or ESC to Quit", True, (255, 255, 255))
            restart_rect = restart_text.get_rect(center=(screenWidth // 2, screenHeight // 2 + 50))
            screen.blit(restart_text, restart_rect)

    run = True
    while run:
        clock.tick(fps)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if game_over:
                    if event.key == pygame.K_r and game_over_timer > game_over_delay:
                        player = reset_game()
                    elif event.key == pygame.K_ESCAPE:
                        run = False
                else:
                    if event.key == pygame.K_SPACE:
                        bullet = player.shoot()
                        if bullet:
                            bullet_group.add(bullet)

        if not game_over:
            for enemy in enemy_group:
                enemy_bullet = enemy.shoot()
                if enemy_bullet:
                    enemy_bullet_group.add(enemy_bullet)

            for bullet in bullet_group:
                hit_enemies = pygame.sprite.spritecollide(bullet, enemy_group, True)
                if hit_enemies:
                    bullet.kill()
                    for enemy in hit_enemies:
                        explosion = Explosion(enemy.rect.centerx, enemy.rect.centery)
                        explosion_group.add(explosion)
            
            if pygame.sprite.spritecollide(player, enemy_bullet_group, True):
                game_over = True
                game_over_timer = 0
                
                explosion = Explosion(player.rect.centerx, player.rect.centery)
                explosion_group.add(explosion)
                
                player.kill()
            
            if len(enemy_group) == 0:
                for i in range(5):
                    enemy = Enemy(100 + i * 80, 100, screenWidth)
                    enemy_group.add(enemy)
            
            player_group.update()
            bullet_group.update()
            enemy_group.update()
            enemy_bullet_group.update()
            explosion_group.update()
        else:
            game_over_timer += clock.get_time()
            
            explosion_group.update()
        
        draw_bg()
        player_group.draw(screen)
        bullet_group.draw(screen)
        enemy_group.draw(screen)
        enemy_bullet_group.draw(screen)
        explosion_group.draw(screen)
        
        if game_over:
            draw_game_over()

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
