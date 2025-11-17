from .base_boss import BaseBoss


class Boss5(BaseBoss):
    """
    Boss 5: "Omega Commander" - Final boss
    
    Features:
    - High health (12 HP) - 12 bullets to kill
    - Simple horizontal movement
    - Rapid firing
    - Gold/yellow color scheme
    
    The final challenge with increased health but simple mechanics.
    """
    
    def __init__(self, screen_width, screen_height):
        # Start boss at top center of screen
        x = screen_width // 2
        y = 50
        super().__init__(x, y, screen_width, screen_height)
    
    def get_max_hp(self):
        """Omega Commander has 12 HP (12 bullets to kill)"""
        return 12
    
    def get_movement_speed(self):
        """Omega Commander moves at normal speed"""
        return 2
    
    def get_shoot_cooldown(self):
        """Omega Commander shoots every 600ms (frequent but manageable)"""
        return 600
    
    def get_boss_color(self):
        """Omega Commander is gold/yellow"""
        return (255, 215, 0)  # Gold
    
    def get_boss_name(self):
        """Return the name of this boss"""
        return "Omega Commander"