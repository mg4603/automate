'''
1) parses command line args
    * save <keyword>- saves the clipboard contents to mcb under keyword
    * list - copies all keywords to clipboard
    * <keyword> - copies val to clipboard
'''
from sys import exit, argv
try:
    from pyperclip import copy, paste
except ImportError:
    exit('This program requires pyperclip.')
from shelve import open

help_msg = '''
python3 mcb.py [-h|--help]          : help menu

Usage:
    python3 mcb.py list             : to list keywords
    python3 mcb.py <keyword>        : to get keyword val
    python3 mcb.py save <keyword>   : save clipboard contents under keyword
    python3 mcb.py delete <keyword> : delete multi-clipboard contents under keyword
    python3 mcb.py delete           : clear multi-clipboard
    
'''

def parse_args(help_msg):
    args = {}
    if len(argv) == 3:
        if argv[1] == 'save':
            args['option'] = 'save'
            args['keyword'] = argv[2]
        elif argv[1] == 'delete':
            args['option'] = 'delete'
            args['keyword'] = argv[2]
        else:
            exit(help_msg)
    elif len(argv) == 2:
        if argv[1] == '-h' or argv[1] == '--help':
            exit(help_msg)
        elif argv[1] == 'list':
            args['option'] = 'list'
            args['keyword'] = ''
        elif argv[1] == 'delete':
            args['option'] = 'delete'
            args['keyword'] = ''
        else:
            args['option'] = ''
            args['keyword'] = argv[1] 
    return args

def main():
    args = parse_args(help_msg)

    mcb = open('mcb')
    
    if args['option'] == 'save':
        mcb[args['keyword']] = paste()
    elif args['option'] == 'list':
        if len(mcb.keys()) == 0:
            exit('Multi-clipboard empty')
        print('\n'.join(mcb.keys()))
    elif args['option'] == '':
        try:
            copy(mcb[args['keyword']])
        except KeyError:
            exit('Key doesn\'t exist\nTo see a list of keys try: python3 mcb.py list ')
    elif args['option'] == 'delete':
        if args['keyword'] != '':
            mcb.pop(args['keyword'])
        else:
            mcb.clear()
    
    mcb.close()

if __name__ == '__main__':
    main()