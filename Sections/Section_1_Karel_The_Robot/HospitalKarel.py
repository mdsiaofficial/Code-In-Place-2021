from karel.stanfordkarel import *

# File: HospitalKarel.py
# -----------------------------
# Here is a place to program your Section problem

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while front_is_clear():
        while no_beepers_present():
            move()
        place_tower()
        if front_is_clear():
            move()

def place_tower():
    turn_left()
    for _ in range(2):
        move()
        put_beeper()
    turn_right()
    move()
    put_beeper()
    turn_right()
    for _ in range(2):
        move()
        put_beeper()
    turn_left()


def turn_right():
    for _ in range(3):
        turn_left()

if __name__ == '__main__':
    run_karel_program('HospitalKarel2.w')
