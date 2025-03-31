# Python Platformer Game
---
A challenging platformer game created with Pygame where players collect coins of different values while avoiding obstacles to reach the top with the fewest attempts and most coins.

<div align="center">
    <img src="https://github.com/user-attachments/assets/4a4d1ed4-4550-4aca-8d6e-2f2faafe0c16">
</div>

## Overview

This project was developed as a final assignment for our Applied Data Structures course. The game is a 2D platformer that demonstrates the practical application of various data structures in game development, including lists, tuples, and object-oriented programming principles.

## Features

- **Character Animation**: Animated player character with movement and idle states
- **Coin Collection**: Collect coins of different values to increase your score
- **Obstacles**: Avoid spikes and other hazards
- **Checkpoints**: Save your progress with strategically placed checkpoints
- **Score Tracking**: Track attempts and coin collection

## Technologies Used

- **Python**: Core programming language
- **Pygame**: Game development framework
- **Object-Oriented Programming**: For code organization and scalability
- **Data Structures**: Practical implementation of lists, tuples, and more

## Project Structure

The game is built following OOP principles, making it easy to understand and modify:

```
Directory structure:
└── josspolanco-py_platformer_game/
    ├── requirements.txt
    ├── assets/
    │   ├── fonts/
    │   │   └── Blocky5x7.ttf
    │   └── img/
    │       ├── Coins/
    │       │   ├── Bronze/
    │       │   ├── Gold/
    │       │   └── Silver/
    │       ├── Objects/
    │       ├── Platforms/
    │       └── Player/
    │           ├── jump/
    │           └── walk/
    └── src/
        ├── __init__.py
        ├── Checkpoint.py
        ├── Coin.py
        ├── Game.py
        ├── main.py
        ├── Platform.py
        ├── Player.py
        ├── settings.py
        ├── Spike.py
        └── utils.py

```

## How to Run

1. Make sure you have Python installed (Python 3.7+ recommended)
2. Install Pygame:
   ```
   pip install pygame
   ```
3. Clone this repository:
   ```
   git clone https://github.com/JossPolanco/py_platformer_game.git
   ```
4. Navigate to the project directory:
   ```
   cd py_platformer_game
   cd src
   ```
5. Run the game:
   ```
   python main.py
   ```

## Game Controls

- **Left/Right Arrow Keys**: Move the character
- **Spacebar**: Jump
- **R**: Restart level
- **ESC**: Pause game

## Learning Outcomes

This project helped us:
- Understand the practical application of data structures
- Learn game development principles using Pygame
- Apply object-oriented programming in a complex project
- Manage project development under time constraints
- Implement animation systems and collision detection

##  Authors

- **Josué Ángel Pérez Polanco**
- **Christian Iván Cisneros Espinoza**

## Future Improvements

- Add more levels
- Implement different character abilities
- Create a level editor
- Add sound effects and background music
- Implement a high score system


## Acknowledgements

- Sprites were obtained from [Unity Asset Store](https://assetstore.unity.com/) and [Itch.io](https://itch.io/)
- Special thanks to our Data Structures professor for the guidance
