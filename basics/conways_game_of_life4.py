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
    print('\n' * 5)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(board[y][x], end='')
        print()

def main():
    board = []

    for y in range(HEIGHT):
        row = []
        for x in range(WIDTH):
            row.append(choice(('#', ' ')))
        board.append(row)
    
    while True:
        draw_board(board)
        next_board = deepcopy(board)
        for y in range(HEIGHT):
            for x in range(WIDTH):
                num_neighbors = 0
                above = y - 1
                below = y + 1
                left = x - 1
                right = x + 1

                if x != 0 and board[y][left] == '#':
                    num_neighbors += 1
                
                if x != WIDTH - 1 and board[y][right] == '#':
                    num_neighbors += 1

                if y != 0 and board[above][x] == '#':
                    num_neighbors += 1

                if y != HEIGHT - 1 and board[below][x] == '#':
                    num_neighbors += 1
                
                if num_neighbors == 3 and board[y][x] == ' ':
                    next_board[y][x] = '#'
                elif (num_neighbors == 2 or num_neighbors == 3) \
                        and next_board[y][x] == '#':
                    next_board[y][x] = '#'
                else:
                    next_board[y][x] = ' '
        board = next_board
        sleep(DELAY)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()