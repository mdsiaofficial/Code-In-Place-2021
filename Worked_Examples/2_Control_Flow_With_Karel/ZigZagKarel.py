from karel.stanfordkarel import *

"""
File: ZigZagKarel.py
-----------------------
Places a zig zag pattern of beepers in the world.
"""

def main():
    # Places beepers in a zig zag pattern.
    zig_one_zag()
    while front_is_clear():
        move()
        zig_one_zag()

def zig_one_zag():
    # Places two beepers at a time. Karel will start and end facing East in row 1.
    # If both beepers can be placed (Karel doesn't start facing a wall), Karel
    # will end up one column greater than where Karel started. If not, Karel
    # will be in the same column as initially.

    put_beeper()
    # Move to row 2
    turn_left()
    move()
    turn_right()
    if front_is_clear(): # If we remove this check, the code will work, but only on even-column-numbered worlds
        # Only move forward a column and place second beeper if Karel isn't already at the rightmost column of the world
        move()
        put_beeper()
    # Move Karel back to row 1
    turn_right()
    move()
    turn_left()


def turn_right():
    for i in range(3):
        turn_left()
if __name__ == "__main__":
    run_karel_program('ZigZag1.w')
