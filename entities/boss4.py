from .base_boss import BaseBoss


class Boss4(BaseBoss):
    """
    Boss 4: "War Machine" - Second boss encounter
    
    Features:
    - Medium health (8 HP) - 8 bullets to kill
    - Simple horizontal movement
    - More frequent shooting
    - Red/orange color scheme
    
    This boss provides a moderate challenge with increased durability.
    """
    
    def __init__(self, screen_width, screen_height):
        # Start boss at top center of screen
        x = screen_width // 2
        y = 50
        super().__init__(x, y, screen_width, screen_height)
    
    def get_max_hp(self):
        """War Machine has 8 HP (8 bullets to kill)"""
        return 8
    
    def get_movement_speed(self):
        """War Machine moves at normal speed"""
        return 2
    
    def get_shoot_cooldown(self):
        """War Machine shoots every 800ms"""
        return 800
    
    def get_boss_color(self):
        """War Machine is red/orange"""
        return (200, 50, 0)  # Red-orange
    
    def get_boss_name(self):
        """Return the name of this boss"""
        return "War Machine"