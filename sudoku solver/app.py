def print_board(board):
    """Prints the Sudoku board in a readable format."""
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty(board):
    """Finds the next empty space (represented by 0) on the board."""
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col
    return None

def is_valid(board, num, pos):
    """Checks if a number can be placed at the given position."""
    row, col = pos

    # Check row
    for j in range(len(board[0])):
        if board[row][j] == num and col != j:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][col] == num and row != i:
            return False

    # Check 3x3 grid
    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(board):
    """Solves the Sudoku puzzle using backtracking."""
    empty = find_empty(board)
    if not empty:
        return True  # Puzzle solved

    row, col = empty

    for num in range(1, 10):  # Try numbers 1 to 9
        if is_valid(board, num, (row, col)):
            board[row][col] = num  # Place the number

            if solve(board):  # Recursive call
                return True

            board[row][col] = 0  # Reset if not valid

    return False  # Trigger backtracking if no number is valid

# Sample Sudoku puzzle (0 represents empty spaces)
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

print("Unsolved Sudoku Board:")
print_board(sudoku_board)

solve(sudoku_board)

print("\nSolved Sudoku Board:")
print_board(sudoku_board)
