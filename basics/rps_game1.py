from random import choice
from sys import exit
from time import sleep

DELAY = 1

def get_move():
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    while True:
        response = input('> ').upper()
        if response == 'Q':
            exit('Thanks for playing!')
        
        elif response in ('R', 'P', 'S'):
            return response
        
        print('Enter one of "R", "P", "S" or "Q"')

def get_word(code):
    assert code in ('R', 'P', 'S'), 'Invalid code'
    if code == 'R':
        return 'ROCK'
    elif code == 'P':
        return 'PAPER'
    elif code == 'S':
        return 'Scissors'

