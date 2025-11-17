from abc import ABC, abstractmethod
import pygame
import random


class BaseBoss(pygame.sprite.Sprite, ABC):
    """
    Abstract Base Class for all boss enemies.
    
    This class provides a template for creating bosses with different configurations
    using inheritance and polymorphism. Each boss can customize:
    - Health points and maximum HP
    - Movement patterns
    - Shooting patterns
    - Size and appearance
    
    Design Principles:
    - Reusability: Common boss logic is implemented once in base class
    - Modularity: Each boss is self-contained with its own configuration
    - Inheritance: Subclasses inherit common behavior and customize specifics
    - Encapsulation: Boss state and logic are encapsulated in the class
    """
    
    def __init__(self, x, y, screen_width, screen_height):
        """
        Initialize the base boss.
        
        Args:
            x: Initial x position
            y: Initial y position
            screen_width: Width of the game screen
            screen_height: Height of the game screen
        """
        super().__init__()
        
        # Position and screen boundaries
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        # Create boss sprite (placeholder rectangle)
        self.image = pygame.Surface((80, 60))
        self.image.fill(self.get_boss_color())
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y
        
        # Health system
        self.max_hp = self.get_max_hp()
        self.current_hp = self.max_hp
        self.is_alive = True
        
        # Movement
        self.speed = self.get_movement_speed()
        self.direction_x = 1  # 1 for right, -1 for left
        self.move_timer = 0
        
        # Shooting
        self.shoot_timer = 0
        self.shoot_cooldown = self.get_shoot_cooldown()
        
        # Animation/visual effects
        self.hit_timer = 0  # For hit flash effect
        self.original_color = self.get_boss_color()
        
    @abstractmethod
    def get_max_hp(self):
        """
        Return the maximum health points for this boss.
        Must be implemented by subclasses.
        """
        pass
    
    @abstractmethod
    def get_movement_speed(self):
        """
        Return the movement speed for this boss.
        Must be implemented by subclasses.
        """
        pass
    
    @abstractmethod
    def get_shoot_cooldown(self):
        """
        Return the shooting cooldown in milliseconds.
        Must be implemented by subclasses.
        """
        pass
    
    @abstractmethod
    def get_boss_color(self):
        """
        Return the color tuple (R, G, B) for this boss.
        Must be implemented by subclasses.
        """
        pass
    
    @abstractmethod
    def get_boss_name(self):
        """
        Return the name of this boss.
        Must be implemented by subclasses.
        """
        pass
    
    def take_damage(self, damage=1):
        """
        Reduce boss health by damage amount.
        
        Args:
            damage: Amount of damage to take (default: 1)
            
        Returns:
            True if boss is still alive, False if defeated
        """
        self.current_hp -= damage
        self.hit_timer = 200  # Flash effect for 200ms
        
        if self.current_hp <= 0:
            self.current_hp = 0
            self.is_alive = False
            
        return self.is_alive
    
    def get_hp_percentage(self):
        """
        Get current HP as a percentage.
        
        Returns:
            Float between 0.0 and 1.0 representing HP percentage
        """
        return self.current_hp / self.max_hp if self.max_hp > 0 else 0.0
    
    def update_movement(self):
        """
        Update boss movement pattern.
        Default implementation: horizontal movement with direction changes at edges.
        Subclasses can override for different movement patterns.
        """
        # Move horizontally
        self.rect.x += self.speed * self.direction_x
        
        # Bounce off screen edges
        if self.rect.left <= 0:
            self.direction_x = 1
            self.rect.left = 0
        elif self.rect.right >= self.screen_width:
            self.direction_x = -1
            self.rect.right = self.screen_width
    
    def update_shooting(self, dt):
        """
        Update shooting timer and create bullets.
        
        Args:
            dt: Delta time in milliseconds
            
        Returns:
            Bullet sprite if boss shoots, None otherwise
        """
        self.shoot_timer += dt
        
        if self.shoot_timer >= self.shoot_cooldown:
            self.shoot_timer = 0
            return self.create_bullet()
        
        return None
    
    def create_bullet(self):
        """
        Create a bullet from the boss.
        Subclasses can override for different bullet patterns.
        
        Returns:
            Bullet sprite
        """
        from entities.enemyBullets import EnemyBullet
        return EnemyBullet(self.rect.centerx, self.rect.bottom)
    
    def update_visual_effects(self, dt):
        """
        Update visual effects like hit flash.
        
        Args:
            dt: Delta time in milliseconds
        """
        if self.hit_timer > 0:
            self.hit_timer -= dt
            # Flash effect - alternate between red and original color
            if (self.hit_timer // 50) % 2:
                self.image.fill((255, 100, 100))  # Red flash
            else:
                self.image.fill(self.original_color)
        else:
            self.image.fill(self.original_color)
    
    def update(self, dt=16):
        """
        Update the boss (movement, shooting, effects).
        
        Args:
            dt: Delta time in milliseconds (default: 16ms for 60 FPS)
        """
        if not self.is_alive:
            return
        
        self.update_movement()
        self.update_visual_effects(dt)
    
    def draw_hp_bar(self, surface, x, y, width=200, height=20):
        """
        Draw the boss HP bar.
        
        Args:
            surface: Surface to draw on
            x: X position of the HP bar
            y: Y position of the HP bar
            width: Width of the HP bar
            height: Height of the HP bar
        """
        # Background (red)
        background_rect = pygame.Rect(x, y, width, height)
        pygame.draw.rect(surface, (200, 50, 50), background_rect)
        
        # Health bar (green to red gradient based on HP)
        hp_percentage = self.get_hp_percentage()
        hp_width = int(width * hp_percentage)
        
        if hp_width > 0:
            hp_rect = pygame.Rect(x, y, hp_width, height)
            # Color changes from green to red as HP decreases
            if hp_percentage > 0.6:
                color = (50, 200, 50)  # Green
            elif hp_percentage > 0.3:
                color = (200, 200, 50)  # Yellow
            else:
                color = (200, 50, 50)  # Red
            pygame.draw.rect(surface, color, hp_rect)
        
        # Border
        pygame.draw.rect(surface, (255, 255, 255), background_rect, 2)
        
        # HP text
        font = pygame.font.Font(None, 24)
        hp_text = font.render(f"{self.current_hp}/{self.max_hp}", True, (255, 255, 255))
        text_rect = hp_text.get_rect(center=(x + width // 2, y + height // 2))
        surface.blit(hp_text, text_rect)
    
    def is_defeated(self):
        """
        Check if the boss is defeated.
        
        Returns:
            True if boss is defeated, False otherwise
        """
        return not self.is_alive