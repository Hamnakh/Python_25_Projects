# Tic-Tac-Toe AI

A Python implementation of the classic Tic-Tac-Toe game with an unbeatable AI opponent using the minimax algorithm.

## Features

- Play against an AI that uses the minimax algorithm
- Clear console-based interface
- Input validation
- Win detection
- Draw detection

## How to Play

1. Run the game using Python:
   ```
   python tic_tac_toe.py
   ```
2. You play as X and the AI plays as O
3. Enter your moves in the format `row,col` where both row and column are numbers from 0 to 2
4. The game will continue until someone wins or it's a draw

## Game Board Layout

```
0,0 | 0,1 | 0,2
-----------------
1,0 | 1,1 | 1,2
-----------------
2,0 | 2,1 | 2,2
```

## How the AI Works

The AI uses the minimax algorithm to make its moves. This algorithm:
- Simulates all possible future game states
- Evaluates each state based on whether it leads to a win, loss, or draw
- Chooses the move that maximizes its chances of winning while minimizing the player's chances

## Requirements

- Python 3.x

## Author

This project is based on Kylie Ying's tutorial on implementing an unbeatable Tic-Tac-Toe AI. 