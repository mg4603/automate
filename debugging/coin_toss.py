from random import randint
from logging import debug, DEBUG, disable, basicConfig, CRITICAL
basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# disable(CRITICAL)

def main():
    print('Guess the coin toss! Enter head or tails:')
    guess = get_guess()
    toss = randint(0, 1)
    if toss == guess:
        print('You got it!')
    else:
        print('Nope! Guess again!')
        guesss = get_guess()
        if toss == guess:
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')

if __name__ == '__main__':
    main()