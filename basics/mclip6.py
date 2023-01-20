#!/usr/bin/env python3
# mclip - a multi-clipboard program
from sys import exit
try:
    from pyperclip import copy
except ImportError:
    exit('This program requires pyperclip.')
from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser(description='Key phrase argument parser')
    parser.add_argument('key_phrase', type=str)
    return parser.parse_args()


def main():
    args = parse_args()
    key = args.key_phrase
    if key in multi_clipboard:
        try:
            copy(multi_clipboard[key])
            print('(Copied {} to clipboard.)'.format(multi_clipboard[key]))
        except NameError:
            exit('This program requires pyperclip')

if __name__ == '__main__':
    main()