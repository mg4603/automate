from pathlib import Path
from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('N', help='row to start insertions after')
    parser.add_argument('M', help='number of blank rows to insert')
    parser.add_argument('file', help='spread sheet to perform insertions on')
    return parser.parse_args()



if __name__ == '__main__':
    main()