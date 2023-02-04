'''
1) read location as command line arg
2) request open weather api for weather data
3) process json data 
4) print weather for the next three days.
'''
from argparse import ArgumentParser
from json import loads

def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        'location', help='location to query weather of'
    )
    return parser.parse_args()
    

if __name__ == '__main__':
    main()