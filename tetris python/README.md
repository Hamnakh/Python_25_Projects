# Python Tetris Game

A classic Tetris game implementation using Python and Pygame. This project is perfect for beginners to learn game development concepts and Python programming.

## Features

- Classic Tetris gameplay with 7 different Tetromino pieces
- Score tracking and level progression
- Smooth controls and piece movement
- Game over detection
- Score and level display
- Colorful pieces and clean interface

## Controls

- **Left Arrow**: Move piece left
- **Right Arrow**: Move piece right
- **Up Arrow**: Rotate piece
- **Down Arrow**: Soft drop (move piece down faster)
- **Space**: Hard drop (instantly drop piece to bottom)

## Installation

1. Make sure you have Python installed on your system
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run

Run the game using Python:
```bash
python tetris.py
```

## Game Rules

- Clear lines by filling them completely with blocks
- Score points for each line cleared
- Game speed increases as you level up
- Game ends when blocks stack up to the top of the screen

## Scoring System

- Each line cleared gives you 100 points multiplied by your current level
- Level increases every 10 lines cleared
- Higher levels mean faster falling pieces

## Requirements

- Python 3.x
- Pygame 2.5.2

## Project Structure

- `tetris.py`: Main game file containing all game logic
- `requirements.txt`: Lists the required Python packages

Enjoy the game! Feel free to modify and enhance it as you learn more about game development. 