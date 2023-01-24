'''
1) get keyword for cmdline or clipboard
2) search on pypi at https://pypi.org/search/?q=
3) open all search links
'''
from sys import exit
try:
    from requests import get
except ImportError:
    exit('This program requires requests.')
try:
    from bs4 import BeautifulSoup
except ImportError:
    exit('This program requires bs4.')
import webbrowser as wb
from argparse import ArgumentParser
try:
    from pyperclip import paste
except ImportError:
    exit('This program requires pyperclip to run.')

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--query', required=False)
    args = parser.parse_args()
    if args.query == None:
        if paste() == '':
            exit('Search query required.')
        return {'query': paste()}
    return {'query': args.query}

def main():
    print('Pypi Search All')
    args = parse_args()

    print('Searching...')
    res = get('https://pypi.org/search/?q={}'.format(args['query']))
    res.raise_for_status()

    soup_obj = BeautifulSoup(res.text, 'html.parser')
    links = soup_obj.select('a.package-snippet')

    for link in links:
        wb.open('https://pypi.org/{}'.format(link.get('href')))
    print('Done')

if __name__ == '__main__':
    main()