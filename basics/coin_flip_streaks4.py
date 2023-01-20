from random import randint

def simulate_flips(num_of_flips):
    flips = []
    for _ in range(num_of_flips):
        if randint(0, 1) == 0:
            flips.append('H')
        else:
            flips.append('T')
    
    return flips