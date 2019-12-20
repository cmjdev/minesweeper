import random
import re

class Cell:
    mine = None
    mines = None

    def __init__(self, mine):
        self.mine = mine

class Game:
    active = True
    tiles = 10
    map = []

    def setup(self):
        # create cells
        tiles = range(self.tiles)
        for y in tiles:
            row = []
            for x in tiles:
                r = random.randint(0, 9)
                row.append(Cell(True) if(r>7) else Cell(False))
            self.map.append(row)

        # find adjacent mines

    def clear(self, x, y):
        if self.map[y][x].mine:
            print("BOOM")
        else: print("nope :(")

    def flag(self, x, y):
        print("you flagged row {} and col {}".format(x,y))

    def do(self, user_input):
        flag = 'f[0-9]+,[0-9]+'
        clear = '^[0-9]+,[0-9]+'

        if re.match(flag, user_input):
            cmd = re.split('f|,', user_input)
            self.flag(int(cmd[1]), int(cmd[2]))
        elif re.match(clear, user_input):
            cmd = re.split(',', user_input)
            self.clear(int(cmd[0]), int(cmd[1]))
        elif user_input == 'exit':
            self.active = False
        else: print("invalid move")

    def user_input(self):
        move = input('> ')
        self.do(move)
    
    def show(self):
        
        # print header
        print(end="  ")
        for i in range(self.tiles):
            print(i, end=" ")
        print()

        map = enumerate(self.map)

        for iy,y in map:
            print(iy, end="|")
            for x in y:
                if x.mine == True:
                    print('*', end="|")
                else: print(end=" |")
            print()


    def run(self):
        while self.active:
            self.show()
            self.user_input()


    def __init__(self):
        self.setup()


game = Game()
game.run()