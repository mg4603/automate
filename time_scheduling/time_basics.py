from time import sleep, time

def sleep_sample():
    for i in range(3):
        print('Tick')
        sleep(1)
        print('Tock')
        sleep(1)

def rounding():
    now = time()
    print(round(now, 2))
    print(round(now, 4))
    print(round(now))

# rounding()
# sleep_sample()