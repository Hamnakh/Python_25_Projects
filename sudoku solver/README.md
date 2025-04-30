Sudoku Solver using Backtracking

Overview

This is a Python-based Sudoku solver that utilizes the Backtracking Algorithm to find solutions to Sudoku puzzles. The program takes an unsolved Sudoku board as input and fills in the missing numbers while following Sudoku rules.

Features

Uses backtracking to efficiently solve Sudoku puzzles.

Handles standard 9x9 Sudoku boards.

Simple command-line interface for easy use.

Prints both the unsolved and solved Sudoku board in a user-friendly format.

How It Works

The algorithm searches for an empty cell (represented by 0).

It tries placing numbers 1-9 and checks if it's a valid move.

If valid, it places the number and recursively tries solving the rest of the board.

If no number works, it backtracks to the previous step and tries a different number.

The process repeats until the entire board is solved.

Installation

To run this Sudoku solver, make sure you have Python installed on your system.

Steps:

Clone this repository or copy the script.

git clone https://github.com/yourusername/sudoku-solver.git
cd sudoku-solver

Run the script:

python sudoku_solver.py

Usage

The program runs in the command line and automatically solves the given Sudoku board.

Modify the sudoku_board variable inside the script to test different puzzles.

Example Input

sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

Example Output

Unsolved Sudoku Board:
5 3 0 | 0 7 0 | 0 0 0
6 0 0 | 1 9 5 | 0 0 0
0 9 8 | 0 0 0 | 0 6 0
---------------------
8 0 0 | 0 6 0 | 0 0 3
4 0 0 | 8 0 3 | 0 0 1
7 0 0 | 0 2 0 | 0 0 6
---------------------
0 6 0 | 0 0 0 | 2 8 0
0 0 0 | 4 1 9 | 0 0 5
0 0 0 | 0 8 0 | 0 7 9

Solved Sudoku Board:
5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
1 9 8 | 3 4 2 | 5 6 7
---------------------
8 5 9 | 7 6 1 | 4 2 3
4 2 6 | 8 5 3 | 7 9 1
7 1 3 | 9 2 4 | 8 5 6
---------------------
9 6 1 | 5 3 7 | 2 8 4
2 8 7 | 4 1 9 | 6 3 5
3 4 5 | 2 8 6 | 1 7 9

Contributing

Feel free to fork the repository and improve the Sudoku solver. Contributions are welcome!

License

This project is open-source and available under the MIT License.

