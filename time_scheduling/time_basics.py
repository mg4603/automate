from time import sleep, time
from datetime import datetime

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

def current_datetime():
    dt = datetime.now()
    print('%s:%s:%s %s/%s/%s' % (
        dt.hour, dt.minute, dt.second,
        dt.day, dt.month, dt.year
    ))

# current_datetime()
# rounding()
# sleep_sample()