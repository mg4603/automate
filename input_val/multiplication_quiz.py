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
try:
    from pyinputplus import inputNum
except ImportError:
    exit('This program requires pyinpuplus to run.')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit('Thanks for playing!')