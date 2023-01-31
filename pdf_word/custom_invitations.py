from argparse import ArgumentParser
from sys import exit
try:
    from docx import Document
except ImportError:
    exit('This program requires python-docx module to run.')

def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        'guest_list', metavar='guest-list',
        help='plaintext file with list of guests to create invitations for'
    )
    parser.add_argument(
        'invitation_doc', metavar='invitation-doc',
        help='word document of invitations to write to.'
    )
    return parser.parse_args()

if __name__ == '__main__':
    main()