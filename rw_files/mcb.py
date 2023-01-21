'''
1) parses command line args
    * save <keyword>- saves the clipboard contents to mcb under keyword
    * list - copies all keywords to clipboard
    * <keyword> - copies val to clipboard
'''
from sys import exit
try:
    from pyperclip import copy, paste
except ImportError:
    exit('This program requires pyperclip.')
from shelve import open


def main():
    args = parse_args()

    mcb = open('mcb')
    
    if args['option'] == 'save':
        mcb[args['keyword']] = paste()
    elif args['options'] == 'list':
        print('\n'.join(mcb.keys()))
    elif args['option'] == '':
        copy(mcb[args['keyword']])
    elif args['option'] == 'delete':
        if args['keyword'] != '':
            mcb.pop(args['keyword'])
        else:
            mcb.clear()
    
    mcb.close()

if __name__ == '__main__':
    main()