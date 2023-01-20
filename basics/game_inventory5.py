def display_inventory(inventory):
    max_length = max(map(len, inventory.keys()))
    total = 0
    print('Inventory:')
    for key, val in inventory.items():
        print('{} {}'.format(key.title().ljust(max_length), val))
        total += val
    print('Total number of items: {}'.format(total))

def main():
    inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inventory = add_to_inventory(inventory, dragon_loot)
    display_inventory(inventory)

if __name__ == '__main__':
    main()