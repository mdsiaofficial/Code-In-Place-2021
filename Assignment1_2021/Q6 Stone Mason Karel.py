from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should be
able to solve the "repair the quad" problem from Assignment 1.
You should make sure that your program works for all of the
sample worlds supplied in the starter folder.
"""


def main():
    repair()  # for the first column

    while front_is_clear():
        if front_is_clear():
            move_to_next_column()  # going to next column
            repair()  # for the second column



def return_home():  # returning to base row...
    turn_around()
    move_to_wall()
    turn_left()


def repair():  # function for repairing columns
    turn_left()
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
            move()
        else:
            move()
    if no_beepers_present():
        put_beeper()
    return_home()


def move_to_next_column():
    for i in range(4):
        move()


def move_to_wall():
    while front_is_clear():
        move()


def turn_around():
    turn_left()
    turn_left()

if __name__ == '__main__':
    run_karel_program('41x41.w')