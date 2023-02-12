from time import sleep

def sleep_sample():
    for i in range(3):
        print('Tick')
        sleep(1)
        print('Tock')
        sleep(1)

# sleep_sample()