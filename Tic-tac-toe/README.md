# Tic-Tac-Toe Game in Python

A simple command-line implementation of the classic Tic-Tac-Toe game built in Python.

## Features

- 🎮 Two-player gameplay
- 📋 Easy-to-understand command-line interface
- ✨ Clean and simple implementation
- ⚡ Input validation and error handling
- 🎯 Win detection for rows, columns, and diagonals
- 🤝 Tie game detection

## How to Play

1. Run the game using Python:
```bash
python tic_tac_toe.py
```

2. The game board is numbered like this:

```
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

3. Players take turns entering numbers (1-9) to place their mark (X or O)
4. First player to get 3 in a row (horizontal, vertical, or diagonal) wins!

## Game Rules

- Player 1 uses 'X'
- Player 2 uses 'O'
- Players alternate turns
- Enter a number between 1-9 to make your move
- You cannot place your mark in an already occupied position
- Game ends when:
  - A player wins by getting 3 in a row
  - The board is full (tie game)

## Requirements

- Python 3.x

## Project Structure

```
tic-tac-toe/
│
├── tic_tac_toe.py    # Main game file
└── README.md         # Project documentation
```

## Functions

The game includes the following main functions:

- `print_board(board)`: Displays the current game board
- `check_winner(board, player)`: Checks if the current player has won
- `is_board_full(board)`: Checks if the board is full (tie game)
- `get_player_move()`: Gets and validates player input
- `main()`: Controls the game flow

## Code Example

Here's a snippet showing how the game board is displayed:

```python
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
```

## Future Improvements

- [ ] Add an AI opponent using minimax algorithm
- [ ] Add a graphical user interface (GUI)
- [ ] Add score tracking
- [ ] Add the ability to play multiple rounds
- [ ] Add different difficulty levels

## Contributing

Feel free to fork this project and make improvements. Pull requests are welcome!

## License

This project is open source and available under the MIT License.

## Author

[Your Name]

## Contact

- Email: [Your Email]
- GitHub: [Your GitHub Profile]

## Acknowledgments

- Thanks to everyone who has contributed to this project
- Inspired by classic Tic-Tac-Toe game

---

Happy Gaming! 🎮