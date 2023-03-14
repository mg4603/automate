from threading import Thread
from time import sleep

def take_nap(seconds):
    sleep(seconds)
    print('Napping thread wakes up!')

def thread_demo():
    print('Thread demo starts')
    thread_obj = Thread(target=take_nap, args=[3])
    thread_obj.start()
    print('End of Thread demo')

# thread_demo()