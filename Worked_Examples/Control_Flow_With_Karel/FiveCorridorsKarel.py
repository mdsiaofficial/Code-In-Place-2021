from karel.stanfordkarel import *

"""
File: FiveCorridorsKarel.py
-----------------------
Karel traverse 5 variable length corridors and place beepers at the ends of them if there aren't already beepers there.
"""

def main():
    for _ in range(5):
        while front_is_clear():
            move()
        if beepers_present():
            move_back()
        else:
            put_beeper()
            move_back()
        if right_is_clear():
            turn_right()
            move()
            turn_right()

    turn_around()

def turn_around():
    turn_left()
    turn_left()
def turn_right():
    for _ in range(3):
        turn_left()
def move_back():
    turn_around()
    while front_is_clear():
        move()


if __name__ == "__main__":
    run_karel_program('Corridors.w')
