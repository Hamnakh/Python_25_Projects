# Python Pong Game

A classic Pong game implementation in Python using the turtle module, inspired by Christian Thompson's tutorial.

## Features

- Two-player gameplay
- Score tracking
- Smooth paddle movement
- Ball physics with bouncing
- Collision detection
- Sound effects (requires bounce.wav file)

## Controls

- Player A (Left Paddle):
  - W: Move paddle up
  - S: Move paddle down

- Player B (Right Paddle):
  - Up Arrow: Move paddle up
  - Down Arrow: Move paddle down

## Requirements

- Python 3.x
- Turtle module (comes with Python standard library)
- bounce.wav file for sound effects (optional)

## Installation

1. Clone or download this repository
2. Make sure you have Python installed on your system
3. Place the `bounce.wav` file in the same directory as `app.py` (optional)

## How to Run

1. Open a terminal/command prompt
2. Navigate to the project directory
3. Run the game using:
   ```
   python app.py
   ```

## Game Rules

- Each player controls a paddle on either side of the screen
- The ball bounces off the top and bottom walls
- If a player misses the ball, the opponent scores a point
- The game continues indefinitely until you close the window

## Customization

You can modify the following aspects of the game:
- Game speed by adjusting `ball.dx` and `ball.dy` values
- Paddle size by changing `stretch_wid` and `stretch_len` values
- Colors by modifying the `color()` parameters
- Screen size by adjusting the `setup()` parameters

## Note

The sound effect uses `afplay` which is for macOS. If you're on Windows, you might want to modify the sound playing code to use a Windows-compatible method or remove the sound effects if you don't need them. 