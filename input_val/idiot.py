'''
1) ask the user if they'd like to know how to keep an idiot busy for hours
2) if no quit
3) if yes goto step 1
'''
from sys import exit
try:
    from pyinputplus import inputYesNo
except ImportError:
    exit('This program requires pyinputplus.')

def main():
    while True:
        prompt = 'Want to know how to keep an idiot busy for hours?\n'
        response = inputYesNo(prompt)
        if response == 'no':
            break
    exit('Thanks for playing!')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit('Thanks for playing!')