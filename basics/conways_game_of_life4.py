from sys import exit
from copy import deepcopy
from time import sleep
from random import choice
DEAD = ' '
ALIVE = '#'

WIDTH = 60
HEIGHT = 40

DELAY = 1

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()