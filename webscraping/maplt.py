'''
1) Get location to search for from commandline or clipboard
2) open webbrowser and search for it at https://www.google.com/maps/search/
'''
from webbrowser import open
from argparse import ArgumentParser
try:
    from pyperclip import paste
except ImportError:
    exit('This program requires pyperclip to run.')

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--location', required=False)

    args = parser.parse_args()
    if args.location == None:
        if paste() == '':
            exit('Location required')

        return {'location': paste()}
        
    return {'location': args.location}

def main():
    print('Google Maps Search')
    args = parse_args()

    open('https://www.google.com/maps/search/{}'.format(args['location']))
    print('Done')

if __name__ == '__main__':
    main()