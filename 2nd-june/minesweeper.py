from dataclasses import dataclass
import random


class Grid():
    def __init__(self, size:int):
        self.__size = size
        self.__mines = size//2
        self.__mines_positions = set()
        self.__cleared_positions = set()
        self.__grid = [["⬛"] * size for _ in range(size)]
        self.__real_grid = [[None] * size for _ in range(size)]

    def display_grid(self):
        last_line = ""
        for i,l in enumerate(self.__grid):
            last_line += str(i+1)+ "  "
            row = ""
            for j in l:
                row += j+" "
            row += str(i+1)
            print(row)
        print(last_line)

    def display_real_grid(self):
        last_line = ""
        for i,l in enumerate(self.__real_grid):
            last_line += str(i+1)+ "  "
            row = ""
            for j in l:
                if isinstance(j,Mine):
                    row += "💣 "
                else:
                    row += "⬜ "
            row += str(i+1)
            print(row)
        print(last_line)
    
    def spawn_mines(self, first_guess:Position):
        spawned_mines = 0
        while spawned_mines < self.__size//2:
            x = random.randint(0,self.__size - 1)
            y = random.randint(0,self.__size - 1)
            if (x,y) not in self.__mines_positions and (first_guess.x != x and first_guess.y != y):
                self.__mines_positions.add((x,y))
                spawned_mines += 1
                self.__real_grid[x][y] = Mine(Position(x,y))
    
    def clear_tiles(self, guess:Position):
        x = guess.x
        y = guess.y
        if (x,y) in self.__mines_positions:
            return True
        surrounding_mines = 0
        pos_to_check = []
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.__size and 0 <= ny < self.__size:
                    if isinstance(self.__real_grid[nx][ny], Mine):
                        surrounding_mines += 1
                    elif self.__grid[nx][ny] != "⬜":
                        pos_to_check.append(Position(nx,ny))
        if surrounding_mines == 0:
            self.__grid[x][y] = "⬜"
            for p in pos_to_check:
                self.clear_tiles(p)
        elif surrounding_mines == 1:
            self.__grid[x][y] = "1️⃣ "
        elif surrounding_mines == 2:
            self.__grid[x][y] = "2️⃣ "
        elif surrounding_mines == 3:
            self.__grid[x][y] = "3️⃣ "
        elif surrounding_mines == 4:
            self.__grid[x][y] = "4️⃣ "
        elif surrounding_mines == 5:
            self.__grid[x][y] = "5️⃣ "
        elif surrounding_mines == 6:
            self.__grid[x][y] = "6️⃣ "
        elif surrounding_mines == 7:
            self.__grid[x][y] = "7️⃣ "
        elif surrounding_mines == 8:
            self.__grid[x][y] = "8️⃣ "
        self.__cleared_positions.add((x,y))
        return False

    
    def play(self):
        is_game_over = False
        self.display_grid()
        guess = input("What is the first area you want you clear ? (x,y) : ")
        x, y = map(int, guess.split(","))
        guess = Position(x-1, y-1)
        self.spawn_mines(guess)
        self.clear_tiles(guess)
        while len(self.__cleared_positions) + self.__mines != self.__size**2 and not is_game_over:
            self.display_grid()
            guess = input("What is the first area you want you clear ? (x,y) : ")
            x, y = map(int, guess.split(","))
            guess = Position(x-1, y-1)
            is_game_over = self.clear_tiles(guess)
        if is_game_over:
            print("A mine detonated. You lose.")
        else:
            print("You cleared out all the mines, congratulation !")
            

class Mine():
    def __init__(self, pos:Position):
        self.__x = pos.x
        self.__y = pos.y

@dataclass
class Position:
    x: int
    y: int

g = Grid(5)

g.play()