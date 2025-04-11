import random
import re

class Minesweeper:
    def __init__(self, dim_size, num_mines):
        self.dim_size = dim_size
        self.num_mines = num_mines
        self.board = []  # board that the user sees
        self.mines = set()  # locations that have mines
        self.dug = set()  # locations that have been dug
        self.initialize_board()

    def initialize_board(self):
        # Create a new board
        self.board = [[' ' for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        
        # Plant the mines
        mines_planted = 0
        while mines_planted < self.num_mines:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size
            
            if (row, col) not in self.mines:
                self.mines.add((row, col))
                mines_planted += 1

    def make_move(self, row, col):
        # Return True if valid move, False if game over
        self.dug.add((row, col))
        
        if (row, col) in self.mines:
            return False
            
        # Count neighboring mines
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) in self.mines:
                    self.board[row][col] = str(self.count_neighboring_mines(row, col))
                    return True
                    
        # If no neighboring mines, recursively dig neighbors
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) not in self.dug:
                    self.make_move(r, c)
                    
        return True

    def count_neighboring_mines(self, row, col):
        count = 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) in self.mines:
                    count += 1
        return count

    def dig(self, row, col):
        # Return True if successful dig, False if game over
        if (row, col) in self.dug:
            return True
            
        self.dug.add((row, col))
        
        if (row, col) in self.mines:
            return False
            
        # Count neighboring mines
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) in self.mines:
                    self.board[row][col] = str(self.count_neighboring_mines(row, col))
                    return True
                    
        # If no neighboring mines, recursively dig neighbors
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) not in self.dug:
                    self.dig(r, c)
                    
        return True

    def __str__(self):
        # Create a string representation of the board
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
                    
        # Put this together in a string
        string_rep = ''
        # Get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key=len)
                )
            )

        # Print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep

def play(dim_size=10, num_mines=10):
    # Initialize the game
    game = Minesweeper(dim_size, num_mines)
    
    # Show the initial board
    print(game)
    
    while True:
        # Get user input
        user_input = re.split(',(\\s)*', input("Enter row,col: "))
        if len(user_input) != 2:
            print("Invalid input! Please enter row,col")
            continue
            
        row, col = int(user_input[0]), int(user_input[1])
        if row < 0 or row >= dim_size or col < 0 or col >= dim_size:
            print("Invalid location! Try again.")
            continue
            
        # Make the move
        safe = game.dig(row, col)
        
        # Check if game is over
        if not safe:
            # Reveal all mines
            for (r, c) in game.mines:
                game.board[r][c] = '*'
            print(game)
            print("GAME OVER!")
            break
            
        # Check if game is won
        if len(game.dug) == dim_size**2 - num_mines:
            print(game)
            print("CONGRATULATIONS! YOU WON!")
            break
            
        # Show the current board
        print(game)

if __name__ == '__main__':
    play() 