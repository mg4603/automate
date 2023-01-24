'''
1) Get location to search for from commandline or clipboard
2) open webbrowser and search for it at https://www.google.com/maps/search/
'''
from webbrowser import open


def main():
    print('Google Maps Search')
    args = parse_args()

    open('https://www.google.com/maps/search/{}'.format(args['location']))
    print('Done')

if __name__ == '__main__':
    main()