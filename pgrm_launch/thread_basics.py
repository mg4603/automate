from threading import Thread
from time import sleep

def take_nap(seconds):
    sleep(seconds)
    print('Napping thread wakes up!')

