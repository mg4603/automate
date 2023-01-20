#!/usr/bin/env python3
# mclip - a multi-clipboard program
from sys import exit
try:
    from pyperclip import copy
except ImportError:
    exit('This program requires pyperclip.')
from argparse import ArgumentParser

multi_clipboard = {
    'agree': """Yes, I agree. That sounds fine to me.""",
    'busy': """Sorry, can we do this later this week or next week?""",
    'upsell': """Would you consider making this a monthly donation?"""
}

def parse_args():
    parser = ArgumentParser(description='Key phrase argument parser')
    help_str = 'Available key phrases: {}'.format(
        ', '.join(multi_clipboard.keys())
    )
    parser.add_argument('key_phrase', type=str, help=help_str)
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
    else:
        print('There is no text for keyphrase: {}'.format(key))

if __name__ == '__main__':
    main()