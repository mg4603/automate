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
    
    def stopwatch(self):
        self.display_intro()
        input()
        print('Started')
        laps = 1
        start_time = time()
        lap_start = start_time
        while True:
            input()
            lap_end = time()
            lap_time = round(lap_end - lap_start , 2)
            total_time = round(lap_end - start_time, 2)
            lap_start = lap_end
            print('lap #%s %s(%s)' %(laps, total_time, lap_time), end='')
            laps += 1
            

def main():
    stopwatch = StopWatch()
    try:
        stopwatch.stopwatch()
    except KeyboardInterrupt:
        exit()

if __name__ == "__main__":
    main()