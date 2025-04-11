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

def get_player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row = move // 3
            col = move % 3
            return row, col
        except ValueError:
            print("Please enter a number between 1 and 9")

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0
    
    print("Welcome to Tic-Tac-Toe!")
    print("Use numbers 1-9 to make your move on the board:")
    print("1 | 2 | 3\n---------\n4 | 5 | 6\n---------\n7 | 8 | 9\n")
    
    while True:
        print_board(board)
        row, col = get_player_move()
        
        if board[row][col] != " ":
            print("That space is already taken! Try again.")
            continue
            
        board[row][col] = players[current_player]
        
        if check_winner(board, players[current_player]):
            print_board(board)
            print(f"Player {players[current_player]} wins!")
            break
            
        if is_board_full(board):
            print_board(board)
            print("Game is a tie!")
            break
            
        current_player = (current_player + 1) % 2

if __name__ == "__main__":
    main()
