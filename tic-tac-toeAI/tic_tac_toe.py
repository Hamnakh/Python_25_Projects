import time
import os
import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_empty_squares(board):
    empty_squares = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                empty_squares.append((i, j))
    return empty_squares

def minimax(board, depth, is_maximizing):
    # Base cases
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if is_board_full(board):
        return 0
    
    if is_maximizing:
        best_score = float("-inf")
        for i, j in get_empty_squares(board):
            board[i][j] = "O"
            score = minimax(board, depth + 1, False)
            board[i][j] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i, j in get_empty_squares(board):
            board[i][j] = "X"
            score = minimax(board, depth + 1, True)
            board[i][j] = " "
            best_score = min(score, best_score)
        return best_score

def get_ai_move(board):
    best_score = float("-inf")
    best_move = None
    
    for i, j in get_empty_squares(board):
        board[i][j] = "O"
        score = minimax(board, 0, False)
        board[i][j] = " "
        
        if score > best_score:
            best_score = score
            best_move = (i, j)
    
    return best_move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("You are X and the AI is O")
    print("Enter your move as row,col (0-2)")
    
    while True:
        print_board(board)
        
        # Player's turn
        while True:
            try:
                row, col = map(int, input("Enter your move (row,col): ").split(","))
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                    break
                else:
                    print("Invalid move! Try again.")
            except ValueError:
                print("Please enter two numbers separated by comma!")
        
        board[row][col] = "X"
        
        # Check if player won
        if check_winner(board, "X"):
            print_board(board)
            print("Congratulations! You won!")
            break
        
        # Check for draw
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # AI's turn
        print("\nAI is thinking...")
        time.sleep(1)
        ai_row, ai_col = get_ai_move(board)
        board[ai_row][ai_col] = "O"
        
        # Check if AI won
        if check_winner(board, "O"):
            print_board(board)
            print("AI wins! Better luck next time!")
            break
        
        # Check for draw
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    main() 