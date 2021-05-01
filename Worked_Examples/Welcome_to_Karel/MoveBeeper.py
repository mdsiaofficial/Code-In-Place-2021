from karel.stanfordkarel import *

"""
File: MoveBeeper.py
------------------------------
Karel will move the beeper up to the top of its column.
Karel starts in the bottom left corner, facing East, in front of the beeper, and Karel will end in the top right corner facing East.
"""


def main():
    find_beeper() # move to beeper and pick it up
    pick_beeper()
    move_to_drop_location() # move up 2 rows
    put_beeper() # put beeper down
    move() # end in top right corner

def find_beeper():
    """ Karel starts facing East in the bottom left of the world and ends up on the beeper, one spot forwards. """
    move()

def move_to_drop_location():
    """ Karel starts facing East in row 1 and ends facing East in row 3. """
    turn_left()
    move()
    move()
    turn_right()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
