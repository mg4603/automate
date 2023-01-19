def collatz(num):
    if type(num) != int:
        raise TypeError('Integer argument expected')

    if num % 2 == 0:
        res = num // 2
        print(res)
        return res
    elif num % 2 == 0:
        res = 3 * num + 1
        print(res)
        return res

def get_number():
    print('Enter a whole number:')
    while True:
        num = input('> ')
        if num.isdecimal():
            return int(num)
        print('Invalid input. Enter a whole number.')
    