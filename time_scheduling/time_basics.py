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

def datetime_obj(
        year, month, day, hour = 0, minute = 0, second = 0
):  
    dt = datetime(year, month, day, hour, minute, second)
    print('%s:%s:%s %s/%s/%s' % (
        str(dt.hour).zfill(2), str(dt.minute).zfill(2),
        str(dt.second).zfill(2), dt.day, dt.month, dt.year
    ))



# datetime_obj(2003, 3, 12)
# datetime_obj(2003, 3, 12, 1)
# datetime_obj(2003, 3, 12, 1, 3)
# datetime_obj(2003, 4, 12, 1, 3, 2)

# current_datetime()
# rounding()
# sleep_sample()