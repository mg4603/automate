from sys import exit
try:
    from pyinputplus import inputNum, inputChoice, inputMenu, inputYesNo
except ImportError:
    exit('This program requires pyinputplus.')

def get_bread_cost(bread):
    if bread == 'wheat':
        return 1.8
    elif bread == 'white':
        return 1
    elif bread == 'sourdough':
        return 2

def get_filling_cost(filling):
    if filling == 'chicken':
        return 2
    elif filling == 'turkey':
        return 3
    elif filling == 'ham':
        return 3.5
    elif filling == 'tofu':
        return 1.5

def main():
    print('Sandwich Maker')

    cost = 0
    
    bread = inputMenu(
        ['wheat', 'white', 'sourdough'],
        prompt='Choose your bread type:\n'
    )
    cost += get_bread_cost(bread)
    print()

    filling = inputMenu(
        ['chicken', 'turkey', 'ham', 'tofu'],
        prompt='Choose your filling:\n'
    )
    cost += get_filling_cost(filling)
    print()

    has_cheese = inputYesNo('Do you want cheese in your sandwich?\n')
    print()

    if has_cheese == 'yes':
        cheese = inputMenu(
            ['cheddar', 'swiss', 'mozzarella'],
            prompt='Choose your type of cheese:\n'
            )
        cost += get_cheese_cost(cheese)
        print()

    has_mayo = inputYesNo('Do you want mayo in your sandwich?\n')
    print()
    has_mustard = inputYesNo('Do you want mustard in your sandwich?\n')
    print()
    has_lettuce = inputYesNo('Do you want lettuce in your sandwich?\n')
    print()
    has_tomato = inputYesNo('Do you want tomato in your sandwich?\n')

    num_sandwiches = inputNum('How many sandwiches do you want?\n')
    print()

    print('Total cost of order:')
    print(cost * num_sandwiches)


if __name__ == '__main__':
    main()