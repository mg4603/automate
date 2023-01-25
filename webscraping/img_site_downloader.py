'''
1) take category as cmdline arg or from clipboard
2) take destination folder
3) search for images
4) download images that match type
'''
from argparse import ArgumentParser
from pathlib import Path
try:
    from requests import get
except ImportError:
    exit('This program requires the requests module.')
try:
    from pyperclip import paste
except ImportError:
    exit('This program requires the pyperclip module.')

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--category', required=False)
    category = parser.parse_args().category
    if category == None:
        if paste() == '':
            exit('No search category given.')
        category = paste()
    return {'category': category}

if __name__ == '__main__':
    main()