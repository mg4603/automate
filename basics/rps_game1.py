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

def main():
    print('ROCK, PAPER, SCISSORS')

    wins = 0
    loss = 0
    ties = 0

    while True:
        print(
            'Wins: %s, Losses: %s, Ties: %s' 
                %
            (wins, loss, ties) 
        )
        move = get_move()
        print('%s versus...' % get_word(move))
        sleep(1)
        computer_move = choice(('R', 'P', 'S'))
        print(get_word(computer_move))

        if move == computer_move:
            ties += 1
            print('It\'s a tie!')
        elif move.lower() == 'r' and computer_move.lower() == 's':
            wins += 1
            print('You win!')
        elif move.lower() == 'p' and computer_move.lower() == 'r':
            wins += 1
            print('You win!')
        elif move.lower() == 's' and computer_move.lower() == 'p':
            wins += 1
            print('You win!')
        elif move.lower() == 's' and computer_move.lower() == 'r':
            loss += 1
            print('You lose!')
        elif move.lower() == 'r' and computer_move.lower() == 'p':
            loss += 1
            print('You lose!')
        elif move.lower() == 'p' and computer_move.lower() == 's':
            loss += 1
            print('You lose!')
