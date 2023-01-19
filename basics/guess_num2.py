from random import randint
from sys import exit

def get_guess(low, high):
    while True:
        print('Take a guess (or QUIT to quit.)')
        response = input('> ').upper()
        if response == 'QUIT':
            exit()
        if response.isdecimal():
            return int(response)
        print(
            'Response should be a number between {} and {}(inclusive).'.format(
                low, high
        ))

def main():
    low = 1
    high = 20
    guesses = 0

    random_num = randint(low, high)

    print('I am thinking of  a number between 1 and 20.')
    while True:
        guess = get_guess(low, high)
        guesses += 1

        if guess < random_num:
            print('Your guess is too low.')
        elif guess > random_num:
            print('Your guess is too high.')
        else:
            if guesses == 1:
                print('Good Job! You guessed my number in {} guesses!'.format(
                    guesses
                ))
            else:
                print('Good job! You guessed my number in {} guess!'.format(
                    guesses
                ))
            break

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()