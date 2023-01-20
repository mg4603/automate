from sys import exit
from random import randint
try:
    from zombiedice.examples import (
        RandomCoinFlipZombie, RollsUntilInTheLeadZombie, 
        MinNumShotgunsThenStopsZombie,
    )
    from zombiedice import runWebGui, runTournament, roll
except ImportError:
    err_msg = '''This program requires the zombie-dice module to run.
Installation instructions can be found at https://pypi.org/project/zombie-dice/

'''
    exit(err_msg)

class RandomContinueZombie:
    def __init__(s, name):
        s.name = name
    
    def turn(s, game_state):
        while True:
            dice_roll_results = roll()
            if randint(0, 1) == 0:
                break

class TwoBrainsThenStopsZombie:
    def __init__(s, name):
        s.name = name
    
    def turn(self, gameState):
        brains = 0
        while True:
            dice_roll_results = roll()

            if dice_roll_results == None:
                return

            brains += dice_roll_results['brains']
            if brains >= 2:
                return

class TwoShotgunsThenStopsZombie:
    def __init__(s, name):
        s.name = name

    def turn(s, game_state):
        shotguns = 0
        while True:
            dice_roll_results = roll()

            if dice_roll_results == None:
                return
            
            shotguns += dice_roll_results['shotgun']
            if shotguns >= 2:
                return

class FourOneRollsWithStopZombie:
    def __init__(s, name):
        s.name = name
    
    def turn(s, game_state):
        num_rolls = randint(1, 4)
        shotguns = 0
        while num_rolls:
            dice_roll_results = roll()
            if dice_roll_results == None:
                return
            
            shotguns += dice_roll_results['shotgun']
            if shotguns >= 2:
                return
            num_rolls -= 1

class MoreShotgunsStopZombie:
    def __init__(s, name):
        s.name = name
    
    def turn(s, game_state):
        brains = 0
        shotguns = 0
        while True:
            dice_roll_result = roll()
            if dice_roll_result == None:
                return
            
            brains += dice_roll_result['brains']
            shotguns += dice_roll_result['shotgun']

            if shotguns > brains:
                return

def main():
    zombies = (
    RandomCoinFlipZombie(name='Random'),
    RollsUntilInTheLeadZombie(name='Until Leading'),
    MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    # Add any other zombie players here.
    RandomContinueZombie(name='Random continue'),
    TwoBrainsThenStopsZombie(name='Stops at 2 brains'),
    TwoShotgunsThenStopsZombie(name='Stops at 2 shotguns - created'),
    FourOneRollsWithStopZombie(name='Rolls 1-4 times but stops at 2 shotguns'),
    MoreShotgunsStopZombie(name='Stops if more shotguns than brains')
    )

    runTournament(zombies=zombies, numGames=1000)
    # runWebGui(zombies=zombies, numGames=1000)

if __name__ == '__main__':
    main()