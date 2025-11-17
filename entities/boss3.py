from .base_boss import BaseBoss


class Boss3(BaseBoss):
    """
    Boss 3: "Guardian Destroyer" - First boss encounter
    
    Features:
    - Low health (5 HP) - easy introduction to bosses
    - Steady movement
    - Regular shooting pattern
    - Purple/blue color scheme
    
    This boss introduces players to boss mechanics without being overwhelming.
    """
    
    def __init__(self, screen_width, screen_height):
        # Start boss at top center of screen
        x = screen_width // 2
        y = 50
        super().__init__(x, y, screen_width, screen_height)
    
    def get_max_hp(self):
        """Guardian Destroyer has 5 HP (5 bullets to kill)"""
        return 5
    
    def get_movement_speed(self):
        """Guardian Destroyer moves at moderate speed"""
        return 2
    
    def get_shoot_cooldown(self):
        """Guardian Destroyer shoots every 1000ms (slower for easier gameplay)"""
        return 1000
    
    def get_boss_color(self):
        """Guardian Destroyer is purple/blue"""
        return (128, 0, 128)  # Purple
    
    def get_boss_name(self):
        """Return the name of this boss"""
        return "Guardian Destroyer"