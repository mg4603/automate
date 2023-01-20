from random import randint

def simulate_flips(num_of_flips):
    flips = []
    for _ in range(num_of_flips):
        if randint(0, 1) == 0:
            flips.append('H')
        else:
            flips.append('T')
    
    return flips

def id_streak(flips, streak_length):
    num_of_streaks = 0
    flips = ''.join(flips)
    head_streak = 'H' * streak_length
    tail_streak = 'T' * streak_length

    for i in range(len(flips) - streak_length + 1):
        if flips[i: i + streak_length] == head_streak or \
                flips[i: i + streak_length] == tail_streak:
            num_of_streaks += 1
    return num_of_streaks

def main():
    num_of_streaks = 0
    total_streaks = 0
    num_of_flips = 100
    streak_length = 6
    for _ in range(10_000):
        num_of_streaks += id_streak(
                simulate_flips(num_of_flips), streak_length
            )
        total_streaks += num_of_flips - streak_length + 1
    
    print('Chance of streak: {}%'.format(num_of_streaks / total_streaks))
    