from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    front_end_beeper()
    org_positon()


def front_end_beeper():
    if no_beepers_present():
        put_beeper()
    while front_is_clear():
        move()
        if front_is_blocked():
            if no_beepers_present():
                put_beeper()
                check_beeper()


def move_till_next_beeper():
    while front_is_clear():
        move()
        if beepers_present():
            check_beeper()


def check_beeper():
    if beepers_present():
        pick_beeper()
        turn_around()
        move()
        conditional_beeper()
        move_till_next_beeper()


def conditional_beeper():
    if no_beepers_present():
        put_beeper()


def org_positon():
    turn_around()
    while no_beepers_present():
        move()


def turn_around():
    turn_left()
    turn_left()
# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
