import random
import re
import string

# row,col to dig ex. 2,1
# frow,col to mark ex. f2,1

TILES = 10

mines = []
active = True

def do_clear(x, y):
    if mines[y][x]:
        print("BOOM")
    else: print("nope :(")

def do_flag(x, y):
    print("you flagged row {} and col {}".format(x,y))

def do(user_input):
    flag = 'f[0-9]+,[0-9]+'
    clear = '^[0-9]+,[0-9]+'

    if re.match(flag, user_input):
        cmd = re.split('f|,', user_input)
        do_flag(int(cmd[1]), int(cmd[2]))
    elif re.match(clear, user_input):
        cmd = re.split(',', user_input)
        do_clear(int(cmd[0]), int(cmd[1]))
    else: print("invalid move")


def build_map(tiles):
    for y in range(tiles):
        row = []
        for x in range(tiles):
            r = random.randint(0, 9)
            row.append(True if(r>7) else False)
        mines.append(row)
        
def show(map):
    print(end="  ")
    for i in range(TILES):
        print(i, end=" ")
    print()

    for i,val in enumerate(map):
        print(i, end="|")
        for doot in val:
            if doot == True:
                print('*', end="|")
            else: print(end=" |")
        print()

build_map(TILES)

while True:
    move = input('> ')
    do(move)
    if move == 'exit': 
        break
    show(mines)