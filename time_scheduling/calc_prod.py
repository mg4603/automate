from time import time

def calc_prod():
    # calculate product of first 100,000 numbers.
    product = 1
    for i in range(1, 100_000):
        product *= i
    return product

def profile_calc_prod():
    start_time = time()

    prod = calc_prod()
    end_time = time()

    print('The result is {} digits long.'.format(len(str(prod))))
    print('Took {} secs to calculate.'.format(end_time - start_time))

def main():
    profile_calc_prod()

if __name__ == '__main__':
    main()