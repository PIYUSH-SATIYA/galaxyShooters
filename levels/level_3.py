from .base_level import BaseLevel


class Level3(BaseLevel):
    """
    Level 3: Advanced - "Invasion Force"
    
    Maximum difficulty with:
    - 15 enemies in three rows (5 per row)
    - Much faster movement (1.6x speed multiplier)
    - Significantly more frequent shooting (2.0x shoot chance multiplier)
    
    The ultimate challenge! Can you survive the full invasion?
    """
    
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height, level_number=3)
    
    def get_level_name(self):
        """Return the name of Level 3"""
        return "Invasion Force"
    
    def get_enemy_count(self):
        """Level 3 has 15 enemies"""
        return 15
    
    def get_enemy_speed_multiplier(self):
        """Level 3 enemies move 60% faster"""
        return 1.6
    
    def get_enemy_shoot_chance_multiplier(self):
        """Level 3 enemies shoot twice as frequently"""
        return 2.0
    
    def get_enemy_positions(self):
        """
        Create three rows of enemies (5 per row).
        Tight formation for maximum threat.
        
        Returns:
            List of (x, y) positions for enemies
        """
        positions = []
        enemies_per_row = 5
        spacing = 80
        row_spacing = 55
        
        # Calculate starting position
        start_x = (self.screen_width - (enemies_per_row - 1) * spacing) // 2
        start_y = 70
        
        # Create three rows of enemies
        for row in range(3):
            y = start_y + row * row_spacing
            # Offset every other row slightly for visual effect
            offset = (spacing // 3) if row % 2 == 1 else 0
            
            for col in range(enemies_per_row):
                x = start_x + col * spacing + offset
                positions.append((x, y))
        
        return positions
