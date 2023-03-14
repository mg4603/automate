from time import sleep, time
from datetime import datetime, timedelta

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

def timestamp_dt(timestamp):
    dt = datetime.fromtimestamp(timestamp)
    datetime_obj(*(dt.year, dt.month, dt.day, 
                   dt.hour, dt.minute, dt.second
                ))

def dt_comparison(dt_one, dt_two):
    if dt_one > dt_two:
        datetime_obj(*(dt_one.year, dt_one.month, dt_one.day,
                       dt_one.hour, dt_one.minute, dt_one.second
                ))
        print('comes later')
    elif dt_two > dt_one:
        datetime_obj(*(dt_two.year, dt_two.month, dt_two.day,
                       dt_two.hour, dt_two.minute, dt_two.second
                ))
        print('comes later')
    else:
        print('Date time objects are identical')

halloween2019 = datetime(2019, 10, 31, 0, 0, 0)
newyears2020 = datetime(2020, 1, 1, 0, 0, 0)
oct31_2019 = datetime(2019, 10, 31, 0, 0, 0)

def add_time_delta(dt_obj, delta):
    dt_obj += delta
    datetime_obj(*(dt_obj.year, dt_obj.month, dt_obj.day,
                   dt_obj.hour, dt_obj.minute, dt_obj.second))

def sub_time_delta(dt_obj, time_delta):
    dt_obj -= time_delta
    datetime_obj(*(dt_obj.year, dt_obj.month, dt_obj.day,
                   dt_obj.hour, dt_obj.minute, dt_obj.second))

# sub_time_delta(datetime.now(), timedelta(days=365))
# add_time_delta(datetime.now(), timedelta(days=1000))
# dt_comparison(halloween2019, oct31_2019)
# dt_comparison(halloween2019, newyears2020)
# timestamp_dt(time())
# timestamp_dt(10000000)
# datetime_obj(2003, 3, 12)
# datetime_obj(2003, 3, 12, 1)
# datetime_obj(2003, 3, 12, 1, 3)
# datetime_obj(2003, 4, 12, 1, 3, 2)

# current_datetime()
# rounding()
# sleep_sample()