from random import randint
from sys import exit

def get_move():
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    while True:
        response = input('> ').upper()
        if response == 'Q':
            exit('Thanks for playing!')
        
        elif response in ('R', 'P', 'S'):
            return response
        
        print('Enter one of "R", "P", "S" or "Q"')
