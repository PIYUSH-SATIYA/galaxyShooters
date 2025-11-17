# Galaxy Shooter - Object-Oriented Game

A space shooter game built with Python and Pygame demonstrating object-oriented programming principles.

## Features

### 5 Levels with Progressive Difficulty

1. **Level 1: First Contact** - Beginner level with 5 enemies, normal speed
2. **Level 2: Escalation** - Intermediate with 10 enemies, 30% faster movement
3. **Level 3: Invasion Force** - Advanced with 15 enemies, 60% faster, 2x shooting
4. **Level 4: Massive Assault** - Expert with 20 enemies in diamond formation
5. **Level 5: Final Confrontation** - Master level with 25 enemies, ultimate challenge

### Menu System

-   **Main Menu** - Start game, select levels, or quit
-   **Level Selection Menu** - Choose any of the 5 levels to play
-   **Level Complete Menu** - 5-second wait timer before allowing progression
-   **Pause Menu** - Pause, resume, restart, or return to main menu
-   **Game Over Menu** - Restart level or return to main menu

### Object-Oriented Design

-   **Inheritance** - All levels inherit from BaseLevel, all menus from BaseMenu
-   **Polymorphism** - Each level has different behaviors while sharing common interface
-   **Encapsulation** - Game logic, level management, and UI are properly separated
-   **Abstraction** - Simple interfaces hide complex implementations

## Controls

### Gameplay

-   **Arrow Keys / WASD** - Move player ship
-   **Spacebar** - Shoot
-   **ESC / P** - Pause game

### Menu Navigation

-   **UP/DOWN or W/S** - Navigate menu options
-   **ENTER/SPACE** - Select option

## Game Flow

1. **Main Menu** - Choose to start game from Level 1 or select any level
2. **Level Selection** - Pick any of the 5 available levels
3. **Gameplay** - Destroy all enemies to complete the level
4. **Level Complete** - Wait 5 seconds, then choose next level, restart, or return to menu
5. **Game Over** - If hit by enemy bullet, restart level or return to main menu

## Level Progression

### Difficulty Scaling

-   **Enemy Count**: 5 → 10 → 15 → 20 → 25
-   **Speed Multiplier**: 1.0x → 1.3x → 1.6x → 1.8x → 2.2x
-   **Shooting Frequency**: 1.0x → 1.5x → 2.0x → 2.5x → 3.0x

### Formation Patterns

-   **Level 1**: Simple horizontal line
-   **Level 2**: Two staggered rows
-   **Level 3**: Three tight rows
-   **Level 4**: Diamond formation
-   **Level 5**: Complex V-formation with multiple layers

## Code Architecture

### Levels (`levels/`)

-   `BaseLevel` - Abstract base class defining level interface
-   `Level1` through `Level5` - Concrete implementations with unique configurations

### Menus (`menus/`)

-   `BaseMenu` - Abstract base class for all menus
-   Specific menus for different game states

### Managers (`managers/`)

-   `LevelManager` - Handles level loading, progression, and statistics

### Entities (`entities/`)

-   Game objects like Player, Enemy, Bullet, etc.

## Installation

1. Install Python 3.7+
2. Install Pygame: `pip install pygame`
3. Run the game: `python main.py`

## File Structure

```
galaxyShooters/
├── main.py                 # Main game loop
├── entities/               # Game objects
├── levels/                 # Level implementations
│   ├── base_level.py      # Abstract base level
│   ├── level_1.py         # Level 1: First Contact
│   ├── level_2.py         # Level 2: Escalation
│   ├── level_3.py         # Level 3: Invasion Force
│   ├── level_4.py         # Level 4: Massive Assault
│   └── level_5.py         # Level 5: Final Confrontation
├── menus/                  # Menu system
│   ├── base_menu.py       # Abstract base menu
│   ├── main_menu.py       # Main menu
│   ├── level_select_menu.py # Level selection
│   └── level_complete_menu.py # Level completion
├── managers/               # Game managers
│   └── level_manager.py   # Level management
└── assets/                 # Game assets
    ├── images/
    └── sounds/
```

## Object-Oriented Principles Demonstrated

1. **Inheritance** - Levels and menus inherit from base classes
2. **Polymorphism** - Different levels behave differently through method overriding
3. **Encapsulation** - Each class manages its own data and behavior
4. **Abstraction** - Complex implementations hidden behind simple interfaces
5. **Composition** - Game uses level manager and menu system
6. **Single Responsibility** - Each class has one clear purpose

## Educational Value

This project demonstrates:

-   Class hierarchy design
-   Abstract base classes and interfaces
-   Method overriding and polymorphism
-   Game state management
-   Modular code organization
-   Reusable components
