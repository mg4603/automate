'''
1) copy from clipboard
2) extract phone nums and emails
3) format them 
4) paste to clipboard
'''
from re import compile, VERBOSE
from sys import exit
try:
    from pyperclip import copy, paste
except ImportError:
    exit('This program requires pyperclip')


if __name__ == '__main__':
    main()