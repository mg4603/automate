from sys import exit
from copy import deepcopy
from time import sleep
from random import choice
DEAD = ' '
ALIVE = '#'

WIDTH = 60
HEIGHT = 40

DELAY = 1

def draw_board(board):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(board[x][y], end='')
        print()
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()