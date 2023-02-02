'''
1) find all csv files in the cwd
2) read csv files
3) remove headers 
4) write to new folder
'''
from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('file', help='csv file to remove header of')
    parser.add_argument(
        '-o', '--output-path', help='output path of header less file'
    )
    return parser.parse_args()

if __name__ == '__main__':
    main()