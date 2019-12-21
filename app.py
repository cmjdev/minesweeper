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
    map = []

    def get_mines(self, cell):

        x = cell.pos[0]
        y = cell.pos[1]

        tiles = self.tiles - 1

        if x > 0:
            cell.mines += self.map[y][x-1].mine
        if x < tiles:
            cell.mines += self.map[y][x+1].mine
        if y > 0 and x > 0:
            cell.mines += self.map[y-1][x-1].mine
        if y > 0:
            cell.mines += self.map[y-1][x].mine
        if y > 0 and x < tiles:
            cell.mines += self.map[y-1][x+1].mine
        if y < tiles and x > 0:
            cell.mines += self.map[y+1][x-1].mine
        if y < tiles:
            cell.mines += self.map[y+1][x].mine
        if y < tiles and x < tiles:
            cell.mines += self.map[y+1][x+1].mine

    def setup(self):
        # create cells
        tiles = range(self.tiles)
        for y in tiles:
            row = []
            for x in tiles:
                r = random.randint(0, 9)
                row.append(Cell(True, (x, y)) if(
                    r > 7) else Cell(False, (x, y)))
            self.map.append(row)

        # find adjacent mines
        for y in self.map:
            for cell in y:
                self.get_mines(cell)

    def clear(self, cell):
        if cell.mine:
            print("BOOM, GAME OVER")
            self.active = False
        else:
            cell.status = "cleared"

    def flag(self, cell):
        print("you flagged {}".format(cell.pos))

    def do(self, user_input):
        flag = 'f[0-9]+,[0-9]+'
        clear = '^[0-9]+,[0-9]+'

        if re.match(flag, user_input):
            cmd = re.split('f|,', user_input)
            self.flag(self.map[int(cmd[2])][int(cmd[1])])
        elif re.match(clear, user_input):
            cmd = re.split(',', user_input)
            self.clear(self.map[int(cmd[1])][int(cmd[0])])
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

        map = enumerate(self.map)

        for iy, y in map:
            print(iy, end="|")
            for cell in y:
                if cell.status == "cleared":
                    if cell.mines > 0:
                        print(cell.mines, end="|")
                    else: print(" ", end="|")
                else: print(".", end="|")
            print()

    def run(self):
        while self.active:
            self.show()
            self.user_input()

    def __init__(self):
        self.setup()


game = Game()
game.run()
