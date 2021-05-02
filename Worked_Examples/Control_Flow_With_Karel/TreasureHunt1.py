from karel.stanfordkarel import *

"""
File: TreasureHunt1.py
------------------------------
Karel will move forward until a beeper.
At every beeper, Karel will turn left and move until the next beeper, until Karel is standing on the treasure, which is a pile of 10 beepers.
"""

def main():
    # Solves treasure map.
    while no_beepers_present():
        move_to_beeper()
        pick_beeper()
        turn_left()

    # Collect treasure!
    while beepers_present():
        pick_beeper()

    # This for loop also works:
    # for i in range(9):
    #     pick_beeper()

def move_to_beeper():
    """ Moves Karel forward until Karel is standing on a beeper. """
    while no_beepers_present():
        move()
if __name__ == "__main__":
    run_karel_program('TreasureHunt1.w')
