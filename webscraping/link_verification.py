'''
1) get url from clipboard or as argument
2) get links on page
3) download every downloadable page and print broken links
'''

from sys import exit
from argparse import ArgumentParser
try:
    from pyperclip import paste
except ImportError:
    exit('This program requires the pyperclip module to run.')
try:
    from requests import get
except ImportError:
    exit('This program requires the requests module to run.')

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('-u', '--url', required=False)
    url = parser.parse_args().url
    if url == None:
        if paste() == '':
            exit('Url required, either as argument or saved to clipboard')
        url = paste()
    return {'url': url}

if __name__ == '__main__':
    main()