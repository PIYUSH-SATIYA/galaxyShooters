#!/usr/bin/env python3
"""
Test script to verify Galaxy Shooter implementation
This script checks the code structure without requiring pygame
"""

import sys
import os

# Add the project root to the Python path
project_root = "/home/piyush/Desktop/projects/objectOrientedDesignandProgramming/galaxyShooters"
sys.path.insert(0, project_root)

def test_imports():
    """Test that all our modules can be imported"""
    try:
        print("Testing level imports...")
        from levels import Level1, Level2, Level3, Level4, Level5
        print("✓ All levels imported successfully")
        
        print("Testing menu imports...")
        from menus import MainMenu, GameOverMenu, PauseMenu, LevelCompleteMenu, LevelSelectMenu
        print("✓ All menus imported successfully")
        
        print("Testing level manager import...")
        from managers.level_manager import LevelManager
        print("✓ Level manager imported successfully")
        
        return True
    except Exception as e:
        print(f"✗ Import error: {e}")
        return False

def test_level_creation():
    """Test that levels can be created"""
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
        
        print(f"✓ Created {len(levels)} levels successfully")
        
        # Test level properties
        for i, level in enumerate(levels, 1):
            print(f"  Level {i}: {level.get_level_name()}")
            print(f"    Enemies: {level.get_enemy_count()}")
            print(f"    Speed multiplier: {level.get_enemy_speed_multiplier()}")
            print(f"    Shoot multiplier: {level.get_enemy_shoot_chance_multiplier()}")
        
        return True
    except Exception as e:
        print(f"✗ Level creation error: {e}")
        return False

def test_level_manager():
    """Test the level manager functionality"""
    try:
        from managers.level_manager import LevelManager
        
        screen_width, screen_height = 600, 800
        level_manager = LevelManager(screen_width, screen_height)
        
        print(f"✓ Level manager created successfully")
        print(f"  Total levels: {level_manager.get_level_count()}")
        
        # Test loading levels
        for i in range(level_manager.get_level_count()):
            level = level_manager.load_level(i)
            if level:
                print(f"  ✓ Level {i+1} loaded: {level.get_level_name()}")
            else:
                print(f"  ✗ Failed to load level {i+1}")
        
        return True
    except Exception as e:
        print(f"✗ Level manager error: {e}")
        return False

def main():
    """Run all tests"""
    print("Galaxy Shooter - Code Structure Test")
    print("=" * 40)
    
    tests = [
        ("Import Test", test_imports),
        ("Level Creation Test", test_level_creation),
        ("Level Manager Test", test_level_manager)
    ]
    
    passed = 0
    for test_name, test_func in tests:
        print(f"\n{test_name}:")
        if test_func():
            passed += 1
    
    print(f"\n" + "=" * 40)
    print(f"Tests passed: {passed}/{len(tests)}")
    
    if passed == len(tests):
        print("✓ All tests passed! The code structure is correct.")
    else:
        print("✗ Some tests failed. Check the errors above.")

if __name__ == "__main__":
    main()