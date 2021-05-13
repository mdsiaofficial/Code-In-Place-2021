from karel.stanfordkarel import *

"""
File: ForLoopWarmup.py
------------------------------
Make Karel place beepers in a square (4 beepers total)
and end in the same position Karel starts in.
"""

def main():
    put_beeper()
    while front_is_clear():
        move()
    if front_is_blocked():
        put_beeper()
        turn_left()
        move()

    while front_is_clear():
        move()
    if front_is_blocked():
        put_beeper()
        turn_left()
        move()

    while front_is_clear():
        move()
    if front_is_blocked():
        put_beeper()
        turn_left()
        move()


if __name__ == "__main__":
    run_karel_program()
