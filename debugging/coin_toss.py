from random import randint
from logging import debug, DEBUG, disable, basicConfig, CRITICAL
basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
disable(CRITICAL)

def get_guess():
    while True:
        guess = input('> ')
        debug('Guess input val: {}'.format(guess))
        if guess in ('heads', 'tails'):
            if guess == 'heads':
                return 1
            else:
                return 0
        print('Invalid input.')

def main():
    print('Guess the coin toss! Enter head or tails:')
    guess = get_guess()
    toss = randint(0, 1)
    debug('Toss:  {}'.format(toss))
    debug('Guess: {}'.format(guess))
    if toss == guess:
        print('You got it!')
    else:
        print('Nope! Guess again!')
        guess = get_guess()
        if toss == guess:
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')

if __name__ == '__main__':
    main()