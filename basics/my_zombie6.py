def main():
    zombies = (
    RandomCoinFlipZombie(name='Random'),
    RollsUntilInTheLeadZombie(name='Until Leading'),
    MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    # Add any other zombie players here.
    RandomContinueZombie(name='Random'),
    TwoBrainsThenStopsZombie(name='Stops at 2 brains'),
    TwoShotgunsThenStopsZombie(name='Stops at 2 shotguns - created'),
    FourOneRollsWithStopZombie(name='Rolls 1-4 times but stops at 2 shotguns'),
    MoreShotgunsStopZombie(name='Stops if more shotguns than brains')
    )

    #runTournament(zombies=zombies, numGames=1000)
    runWebGui(zombies=zombies, numGames=1000)
    