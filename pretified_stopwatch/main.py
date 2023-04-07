from time import time

def stopwatch():
    print('Press ENTER to start the stopwatch.')
    print('Afterwards, press ENTER to start a new lap.')
    print('Press Ctrl-C to quit.')
    print()
    input()
    print('Started')
    
    laps = 1
    start_time = time()
    lap_start = start_time
    while True:
        input()
        current_time = time()
        print('Lap #%s: %s (%s)'%(
            str(round(laps, 2)).rjust(3),
            str(round(current_time - start_time, 2)).rjust(4),
            str(round(current_time - lap_start, 2)).rjust(4)
        ), end='')
        laps += 1

def main():
    print('Stopwatch')
    stopwatch()

if __name__ == '__main__':
    main()