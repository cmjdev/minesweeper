import random
import re


class Cell:
    pos = ()
    mine = None
    mines = 0
    status = None

    def __init__(self, mine, pos):
        self.mine = mine
        self.pos = pos


class Game:

    active = True
    tiles = 10
    mines = 0
    cleared = 0
    cells = []

    def get_mines(self, cell):

        x = cell.pos[0]
        y = cell.pos[1]

        tiles = self.tiles - 1

        if x > 0:
            cell.mines += self.cells[y][x-1].mine
        if x < tiles:
            cell.mines += self.cells[y][x+1].mine
        if y > 0 and x > 0:
            cell.mines += self.cells[y-1][x-1].mine
        if y > 0:
            cell.mines += self.cells[y-1][x].mine
        if y > 0 and x < tiles:
            cell.mines += self.cells[y-1][x+1].mine
        if y < tiles and x > 0:
            cell.mines += self.cells[y+1][x-1].mine
        if y < tiles:
            cell.mines += self.cells[y+1][x].mine
        if y < tiles and x < tiles:
            cell.mines += self.cells[y+1][x+1].mine

    def setup(self):
        # create cells
        tiles = range(self.tiles)
        for y in tiles:
            row = []
            for x in tiles:
                r = random.randint(0, 9)
                if r > 8:
                    row.append(Cell(True, (x, y)))
                    self.mines += 1
                else:
                    row.append(Cell(False, (x, y)))

            self.cells.append(row)

        # find adjacent mines
        for y in self.cells:
            for cell in y:
                self.get_mines(cell)

    def clear(self, cell):

        if not cell.status == "cleared":

            self.cleared += 1

            if cell.mine:
                print("BOOM, GAME OVER")
                self.active = False
            elif cell.mines:
                cell.status = "cleared"
            else:
                cell.status = "cleared"
                tiles = self.tiles - 1

                x = cell.pos[0]
                y = cell.pos[1]

                if x > 0:
                    self.clear(self.cells[y][x-1])
                if x < tiles:
                    self.clear(self.cells[y][x+1])
                if y > 0 and x > 0:
                    self.clear(self.cells[y-1][x-1])
                if y > 0:
                    self.clear(self.cells[y-1][x])
                if y > 0 and x < tiles:
                    self.clear(self.cells[y-1][x+1])
                if y < tiles and x > 0:
                    self.clear(self.cells[y+1][x-1])
                if y < tiles:
                    self.clear(self.cells[y+1][x])
                if y < tiles and x < tiles:
                    self.clear(self.cells[y+1][x+1])

        uncleared = self.tiles * self.tiles - self.cleared

        if self.mines == uncleared:
            print("AREA ALL CLEAR. YOU LIVE!")
            self.active = False

    def flag(self, cell):
        if cell.status != "cleared":
            cell.status = "flagged"

    def do(self, user_input):
        flag = 'f[0-9]+,[0-9]+'
        clear = '^[0-9]+,[0-9]+'

        if re.match(flag, user_input):
            cmd = re.split('f|,', user_input)
            self.flag(self.cells[int(cmd[2])][int(cmd[1])])
        elif re.match(clear, user_input):
            cmd = re.split(',', user_input)
            self.clear(self.cells[int(cmd[1])][int(cmd[0])])
        elif user_input == 'exit':
            self.active = False
        else:
            print("invalid move")

    def user_input(self):
        self.do(input('> '))

    def show(self):

        # print header
        print(end="  ")
        for i in range(self.tiles):
            print(i, end=" ")
        print()

        cells = enumerate(self.cells)

        for iy, y in cells:
            print(iy, end="|")
            for cell in y:
                if cell.status == "cleared":
                    if cell.mines > 0:
                        print(cell.mines, end="|")
                    else:
                        print(" ", end="|")
                elif cell.status == "flagged":
                    print("F", end="|")
                else:
                    print(".", end="|")
            print()

    def run(self):
        while self.active:
            self.show()
            self.user_input()

    def __init__(self):
        self.setup()


game = Game()
game.run()
