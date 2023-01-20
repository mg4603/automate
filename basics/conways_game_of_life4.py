from sys import exit
from copy import deepcopy
from time import sleep
DEAD = ' '
ALIVE = '#'

WIDTH = 60



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()