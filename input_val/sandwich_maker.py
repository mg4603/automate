from sys import exit
try:
    from pyinputplus import inputNum, inputChoice, inputMenu
except ImportError:
    exit('This program requires pyinputplus.')

if __name__ == '__main__':
    main()