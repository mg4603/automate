'''
1) get keyword for cmdline or clipboard
2) search on pypi at https://pypi.org/search/?q=
3) open all search links
'''
import webbrowser as wbrowser
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
    return args

def main():
    print('Pypi Search All')
    args = parse_args()

    wbrowser.open('https://pypi.org/search/?q={}'.format(args['query']))
    print('Done')

if __name__ == '__main__':
    main()