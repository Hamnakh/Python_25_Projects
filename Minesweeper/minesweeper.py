import random

class Minesweeper:
    def __init__(self, dim_size, num_mines):
        self.dim_size = dim_size
        self.num_mines = num_mines
        self.board = [[' ' for _ in range(dim_size)] for _ in range(dim_size)]
        self.mines = set()
        self.dug = set()
        self.plant_mines()

    def plant_mines(self):
        planted = 0
        while planted < self.num_mines:
            loc = random.randint(0, self.dim_size**2 - 1)
            row, col = divmod(loc, self.dim_size)
            if (row, col) in self.mines:
                continue
            self.mines.add((row, col))
            planted += 1

    def dig(self, row, col):
        if (row, col) in self.dug:
            return True
        self.dug.add((row, col))
        if (row, col) in self.mines:
            return False
        count = self.get_num_neighbor_mines(row, col)
        self.board[row][col] = str(count)
        if count == 0:
            for r in range(max(0, row - 1), min(self.dim_size, row + 2)):
                for c in range(max(0, col - 1), min(self.dim_size, col + 2)):
                    if (r, c) not in self.dug:
                        self.dig(r, c)
        return True

    def get_num_neighbor_mines(self, row, col):
        count = 0
        for r in range(max(0, row - 1), min(self.dim_size, row + 2)):
            for c in range(max(0, col - 1), min(self.dim_size, col + 2)):
                if (r, c) != (row, col) and (r, c) in self.mines:
                    count += 1
        return count

    def __str__(self):
        visible = [[' ' if (r, c) not in self.dug else self.board[r][c]
                    for c in range(self.dim_size)]
                   for r in range(self.dim_size)]
        s = '   ' + ' '.join(str(i) for i in range(self.dim_size)) + '\n'
        s += '  ' + '--' * self.dim_size + '\n'
        for i, row in enumerate(visible):
            s += f"{i}| " + ' '.join(row) + '\n'
        return s


def play(dim_size=10, num_mines=10):
    game = Minesweeper(dim_size, num_mines)
    print(game)

    while True:
        try:
            user_input = input("Enter row,col: ").strip().split(',')
            if len(user_input) != 2:
                raise ValueError

            row = int(user_input[0].strip())
            col = int(user_input[1].strip())

            if row < 0 or row >= dim_size or col < 0 or col >= dim_size:
                print("Invalid location! Try again.")
                continue

        except ValueError:
            print("Invalid input! Please enter row,col")
            continue

        safe = game.dig(row, col)

        if not safe:
            for (r, c) in game.mines:
                game.board[r][c] = '*'
            print(game)
            print("GAME OVER!")
            break

        if len(game.dug) == dim_size**2 - num_mines:
            print(game)
            print("CONGRATULATIONS! YOU WON!")
            break

        print(game)


if __name__ == '__main__':
    play()
