import pygame
import random
from pygame.locals import *
from entities.player import Player
from entities.enemy import Enemy
from entities.explosion import Explosion
from menus import MainMenu, GameOverMenu, PauseMenu, LevelCompleteMenu
from levels import Level1, Level2, Level3

# Game states
MAIN_MENU = "MAIN_MENU"
PLAYING = "PLAYING"
PAUSED = "PAUSED"
GAME_OVER = "GAME_OVER"
LEVEL_COMPLETE = "LEVEL_COMPLETE"

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
    
    # Initialize menus
    main_menu = MainMenu(screenWidth, screenHeight)
    game_over_menu = GameOverMenu(screenWidth, screenHeight)
    pause_menu = PauseMenu(screenWidth, screenHeight)
    level_complete_menu = LevelCompleteMenu(screenWidth, screenHeight)
    
    # Game state
    current_state = MAIN_MENU
    
    # Level system
    available_levels = [
        Level1(screenWidth, screenHeight),
        Level2(screenWidth, screenHeight),
        Level3(screenWidth, screenHeight)
    ]
    current_level_index = 0
    current_level = None

    # Game variables (initialized when starting game)
    player = None
    player_group = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    enemy_bullet_group = pygame.sprite.Group()
    explosion_group = pygame.sprite.Group()

    def initialize_game(level_index=0):
        """
        Initialize/reset the game to starting state with specified level.
        
        Args:
            level_index: Index of the level to start (0 = Level 1, 1 = Level 2, etc.)
        """
        nonlocal player, current_level, current_level_index
        
        # Set the current level
        current_level_index = level_index
        current_level = available_levels[current_level_index]
        
        # Clear all sprite groups
        bullet_group.empty()
        enemy_group.empty()
        enemy_bullet_group.empty()
        explosion_group.empty()
        player_group.empty()
        
        # Create new player
        player = Player(screenWidth // 2, screenHeight - 130, screenWidth)
        player_group.add(player)
        
        # Spawn level enemies
        current_level.spawn_enemies()
        # Copy enemies from level to game enemy_group
        for enemy in current_level.enemy_group:
            enemy_group.add(enemy)
        
        # Reset game over menu timer
        game_over_menu.reset_timer()

    run = True
    while run:
        dt = clock.tick(fps)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                # Handle state-specific input
                if current_state == MAIN_MENU:
                    action = main_menu.handle_input(event)
                    if action == "START_GAME":
                        initialize_game()
                        current_state = PLAYING
                    elif action == "QUIT_GAME":
                        run = False
                
                elif current_state == PLAYING:
                    # Pause key
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                        current_state = PAUSED
                    # Shooting
                    elif event.key == pygame.K_SPACE:
                        bullet = player.shoot()
                        if bullet:
                            bullet_group.add(bullet)
                
                elif current_state == PAUSED:
                    # Resume with ESC or P
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                        current_state = PLAYING
                    else:
                        action = pause_menu.handle_input(event)
                        if action == "RESUME_GAME":
                            current_state = PLAYING
                        elif action == "RESTART_GAME":
                            initialize_game()
                            current_state = PLAYING
                        elif action == "MAIN_MENU":
                            current_state = MAIN_MENU
                
                elif current_state == GAME_OVER:
                    action = game_over_menu.handle_input(event)
                    if action == "RESTART_GAME":
                        initialize_game(current_level_index)
                        current_state = PLAYING
                    elif action == "MAIN_MENU":
                        current_state = MAIN_MENU
                
                elif current_state == LEVEL_COMPLETE:
                    action = level_complete_menu.handle_input(event)
                    if action == "NEXT_LEVEL":
                        # Load next level
                        initialize_game(current_level_index + 1)
                        current_state = PLAYING
                    elif action == "RESTART_LEVEL":
                        # Restart current level
                        initialize_game(current_level_index)
                        current_state = PLAYING
                    elif action == "MAIN_MENU":
                        current_state = MAIN_MENU

        # Update game logic based on current state
        if current_state == PLAYING:
            # Enemy shooting
            for enemy in enemy_group:
                enemy_bullet = enemy.shoot()
                if enemy_bullet:
                    enemy_bullet_group.add(enemy_bullet)

            # Bullet-enemy collision
            for bullet in bullet_group:
                hit_enemies = pygame.sprite.spritecollide(bullet, enemy_group, True)
                if hit_enemies:
                    bullet.kill()
                    for enemy in hit_enemies:
                        explosion = Explosion(enemy.rect.centerx, enemy.rect.centery)
                        explosion_group.add(explosion)
                        # Track enemy kill in level
                        current_level.enemy_killed()
            
            # Player-enemy bullet collision (game over)
            if pygame.sprite.spritecollide(player, enemy_bullet_group, True):
                explosion = Explosion(player.rect.centerx, player.rect.centery)
                explosion_group.add(explosion)
                player.kill()
                game_over_menu.reset_timer()
                current_state = GAME_OVER
            
            # Check for level completion
            if len(enemy_group) == 0 and current_level is not None:
                current_level.is_complete = True
                level_complete_menu.set_level_info(
                    current_level.level_number,
                    current_level.get_level_name()
                )
                current_state = LEVEL_COMPLETE
            
            # Update all game sprites
            player_group.update()
            bullet_group.update()
            enemy_group.update()
            enemy_bullet_group.update()
            explosion_group.update()
            
            # Update level
            if current_level is not None:
                current_level.update()
        
        elif current_state == GAME_OVER:
            # Only update explosions in game over state
            explosion_group.update()
            game_over_menu.update(dt)
        
        elif current_state == LEVEL_COMPLETE:
            # Update explosions in level complete state
            explosion_group.update()

        # Drawing
        draw_bg()
        
        if current_state in [PLAYING, PAUSED, GAME_OVER, LEVEL_COMPLETE]:
            # Draw game objects
            player_group.draw(screen)
            bullet_group.draw(screen)
            enemy_group.draw(screen)
            enemy_bullet_group.draw(screen)
            explosion_group.draw(screen)
            
            # Draw level info HUD during gameplay
            if current_state == PLAYING and current_level is not None:
                level_info = f"Level {current_level.level_number}: {current_level.get_level_name()}"
                level_text = small_font.render(level_info, True, (255, 255, 255))
                screen.blit(level_text, (10, 10))
                
                # Draw enemy count
                progress = current_level.get_progress()
                enemy_text = small_font.render(f"Enemies: {len(enemy_group)}/{progress[1]}", True, (255, 255, 255))
                screen.blit(enemy_text, (10, 40))
        
        # Draw menus on top
        if current_state == MAIN_MENU:
            main_menu.draw(screen)
        elif current_state == PAUSED:
            pause_menu.draw(screen)
        elif current_state == GAME_OVER:
            game_over_menu.draw(screen)
        elif current_state == LEVEL_COMPLETE:
            level_complete_menu.draw(screen)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
