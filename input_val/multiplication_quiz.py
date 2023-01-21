'''
multiplication quiz

1) pick two random numbers
2) ask the user the product
3) if correct, record
4) if incorrect, prompt
5) set time limit per question to 8 secs
6) set tries limit to 3
'''
from sys import exit
from random import randint
from time import sleep
try:
    from pyinputplus import inputNum, RetryLimitException, TimeoutException
except ImportError:
    exit('This program requires pyinpuplus to run.')

DELAY = 1

def main():
    score = 0
    num_of_questions = 10
    for i in range(num_of_questions):
        num1 = randint(1, 9)
        num2 = randint(1, 9)
        try:
            prompt = '#{}: {} x {}'.format(i + 1, num1, num2)
            inputNum(
                prompt, 
                allowRegexes='^{}$'.format(num1 * num2),
                blockRegexes=('.*', 'Incorrect!')
            )
        except RetryLimitException:
            print('Out of tries!')
        except TimeoutException:
            print('Out of time!')
        else:
            print('Correct!')
            score += 1
        sleep(DELAY)
    print('Score: {} / {}'.format(score, num_of_questions))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit('Thanks for playing!')