'''
1. track the amount of time between each key press
2. print lap number, total time, lap time
'''
from time import time
from sys import exit

class StopWatch:
    def __init__(self):
        pass

    def display_intro(self):
        print('Press ENTER to begin.')
        print('Afterward, press ENTER to "click" the stopwatch.')
        print('Press Ctrl-C to quit.')
        print()


def main():
    stopwatch = StopWatch()
    try:
        stopwatch.stopwatch()
    except KeyboardInterrupt:
        exit()

if __name__ == "__main__":
    main()