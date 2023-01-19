def collatz(num):
    if type(num) != int:
        raise TypeError('Integer argument expected')

    if num % 2 == 0:
        res = num // 2
        return res
    elif num % 2 == 1:
        res = 3 * num + 1
        return res

def get_number():
    print('Enter a whole number:')
    while True:
        num = input('> ')
        if num.isdecimal():
            return int(num)
        print('Invalid input. Enter a whole number.')

def main():
    
    print('Collatz Sequence')
    number = get_number()

    while number != 1:
        print(number, end=', ', flush=True)
        number = collatz(number)
        if number == 1:
            print(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()