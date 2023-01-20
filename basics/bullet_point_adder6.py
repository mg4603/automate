from sys import exit
try:
    from pyerclip import copy, paste
except ImportError:
    exit('This script requires pyperclip.')



if __name__ == '__main__':
    main()