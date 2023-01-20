def display_inventory(inventory):
    max_length = max(map(len, inventory.keys()))
    total = 0
    print('Inventory:')
    for key, val in inventory.items():
        print('{} {}'.format(key.title().ljust(max_length), val))
        total += val
    print('Total number of items: {}'.format(total))

def main():
    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    display_inventory(stuff)

if __name__ == '__main__':
    main()