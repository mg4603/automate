'''
1) get keyword for cmdline or clipboard
2) search on pypi at https://pypi.org/search/?q=
3) open all search links
'''

def main():
    print('Pypi Search All')
    args = parse_args()

    wbrowser.open('https://pypi.org/search/?q={}'.format(args['q']))
    print('Done')

if __name__ == '__main__':
    main()