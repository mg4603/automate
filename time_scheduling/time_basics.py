from time import time

def calc_prod():
    # calculate product of first 100,000 numbers.
    product = 1
    for i in range(1, 100_000):
        product *= i
    return product