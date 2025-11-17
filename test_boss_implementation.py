#!/usr/bin/env python3
"""
Test script for Galaxy Shooter boss implementation
This script checks the boss and level structure without requiring pygame
"""

import sys
import os

# Add the project root to the Python path
project_root = "/home/piyush/Desktop/projects/objectOrientedDesignandProgramming/galaxyShooters"
sys.path.insert(0, project_root)

def test_boss_imports():
    """Test that all boss classes can be imported"""
    try:
        print("Testing boss imports...")
        from entities.base_boss import BaseBoss
        from entities.boss3 import Boss3
        from entities.boss4 import Boss4
        from entities.boss5 import Boss5
        print("✓ All boss classes imported successfully")
        
        return True
    except Exception as e:
        print(f"✗ Boss import error: {e}")
        return False

def test_boss_creation():
    """Test that bosses can be created"""
    try:
        from entities.boss3 import Boss3
        from entities.boss4 import Boss4
        from entities.boss5 import Boss5
        
        screen_width, screen_height = 600, 800
        
        bosses = [
            Boss3(screen_width, screen_height),
            Boss4(screen_width, screen_height),
            Boss5(screen_width, screen_height)
        ]
        
        print(f"✓ Created {len(bosses)} bosses successfully")
        
        # Test boss properties
        for i, boss in enumerate(bosses, 3):
            print(f"  Boss {i}: {boss.get_boss_name()}")
            print(f"    Max HP: {boss.get_max_hp()}")
            print(f"    Speed: {boss.get_movement_speed()}")
            print(f"    Shoot Cooldown: {boss.get_shoot_cooldown()}ms")
            print(f"    Color: {boss.get_boss_color()}")
        
        return True
    except Exception as e:
        print(f"✗ Boss creation error: {e}")
        return False

def test_level_boss_integration():
    """Test that levels properly integrate with bosses"""
    try:
        from levels import Level1, Level2, Level3, Level4, Level5
        
        screen_width, screen_height = 600, 800
        
        levels = [
            Level1(screen_width, screen_height),
            Level2(screen_width, screen_height),
            Level3(screen_width, screen_height),
            Level4(screen_width, screen_height),
            Level5(screen_width, screen_height)
        ]
        
        print("✓ Level-Boss integration test:")
        
        for level in levels:
            has_boss = level.level_has_boss()
            boss_name = "None"
            if has_boss:
                boss = level.create_boss()
                if boss:
                    boss_name = boss.get_boss_name()
            
            print(f"  {level.get_level_name()}: Boss = {boss_name}")
        
        return True
    except Exception as e:
        print(f"✗ Level-boss integration error: {e}")
        return False

def test_difficulty_progression():
    """Test the difficulty progression across levels"""
    try:
        from levels import Level1, Level2, Level3, Level4, Level5
        
        screen_width, screen_height = 600, 800
        
        levels = [
            Level1(screen_width, screen_height),
            Level2(screen_width, screen_height),
            Level3(screen_width, screen_height),
            Level4(screen_width, screen_height),
            Level5(screen_width, screen_height)
        ]
        
        print("✓ Difficulty progression test:")
        print(f"{'Level':<8} {'Name':<20} {'Enemies':<8} {'Speed':<7} {'Shooting':<9} {'Boss':<15}")
        print("-" * 75)
        
        for level in levels:
            boss_name = "None"
            if level.level_has_boss():
                boss = level.create_boss()
                if boss:
                    boss_name = boss.get_boss_name()
            
            print(f"{level.level_number:<8} {level.get_level_name():<20} "
                  f"{level.get_enemy_count():<8} {level.get_enemy_speed_multiplier():<7.1f} "
                  f"{level.get_enemy_shoot_chance_multiplier():<9.1f} {boss_name:<15}")
        
        return True
    except Exception as e:
        print(f"✗ Difficulty progression error: {e}")
        return False

def main():
    """Run all tests"""
    print("Galaxy Shooter - Boss Implementation Test")
    print("=" * 50)
    
    tests = [
        ("Boss Import Test", test_boss_imports),
        ("Boss Creation Test", test_boss_creation),
        ("Level-Boss Integration Test", test_level_boss_integration),
        ("Difficulty Progression Test", test_difficulty_progression)
    ]
    
    passed = 0
    for test_name, test_func in tests:
        print(f"\n{test_name}:")
        if test_func():
            passed += 1
    
    print(f"\n" + "=" * 50)
    print(f"Tests passed: {passed}/{len(tests)}")
    
    if passed == len(tests):
        print("✓ All tests passed! Boss implementation is ready!")
    else:
        print("✗ Some tests failed. Check the errors above.")

if __name__ == "__main__":
    main()