'''
1. get countdown time
2. count down to 0
3. play a sound file when the countdown reaches zero
'''
from subprocess import Popen
from shlex import split
from time import sleep
from datetime import datetime
from logging import debug, basicConfig, disable, DEBUG, CRITICAL
basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
disable(CRITICAL)

def get_num(prompt):
    while True:
        num = input(prompt)
        try:
            num = int(num)
            if (0 <= num <=60):
                return num
            print('Invalid input: 0-60')
        except:
            print('Invalid input: enter a number')

def get_countdown_time():
    print('Enter hours:')
    prompt = '> '
    h = get_num(prompt)
    print('Enter minutes:')
    m = get_num(prompt)
    print('Enter seconds:')
    s = get_num(prompt)
    debug('hours: %s' % h)
    debug('minutes: %s' % m)
    debug('seconds: %s' % s)
    return h, m, s

def countdown(h, m, s):
    if h > 99:
        print('Maximum hours: 99')
        h = 99
    
    debug('%s:%s:%s' %(h, m, s))
    while h or m or s:
        print('%s:%s:%s' % (
            str(h).zfill(2), str(m).zfill(2),
            str(s).zfill(2)
        ),end='\r')
        if s == 0:
            if m == 0:
                h -= 1
                m = 59
                s = 60
            else:
                m -= 1
                s = 60
        s -= 1
        sleep(1)    

def main():
    print('Countdown Timer')
    h, m, s = get_countdown_time()
    countdown(h, m, s)
    proc = Popen(split('see alarm.wav'))
    proc.wait()

if __name__ == '__main__':
    main()