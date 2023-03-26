'''
1. get countdown time
2. count down to 0
3. play a sound file when the countdown reaches zero
'''

def main():
    print('Countdown Timer')
    h, m, s = get_countdown_time()
    countdown()
    proc = Popen(split('see '))
    proc.wait()

if __name__ == '__main__':
    main()