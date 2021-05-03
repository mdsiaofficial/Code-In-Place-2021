from karel.stanfordkarel import *

"""
File: UpstairsDownstairs.py
------------------------------
Karel will climb three stair steps up and then three stair steps down.
"""

def main():
    climb_mountain()
    raise_flag()
    climb_down()


def climb_mountain():
    # preconditon: karel is at the bottom of the countain
    while front_is_blocked():
        step_up()

def climb_down():
    while front_is_clear():
        step_down()

def step_up():
    # karel must be facing east
    turn_left()
    move()
    turn_right()
    move()

def step_down():
    # going down
    # pre: karel is on the top of the mountain
    # post: karel will go down
    move()
    turn_right()
    move()
    turn_left()

def raise_flag():
    # putting a beeper as a flag
    put_beeper()

def turn_right():
    for _ in range(3):
        turn_left()



























"""    turn_left()
    while front_is_clear():
        move()
    if front_is_blocked():
        turn_left()
        turn_left()
        turn_left()
    while front_is_clear():
        move()
    if front_is_blocked():
        turn_left()
        turn_left()
        turn_left()
        while front_is_clear():
            move()
        if front_is_blocked():
            turn_left()
            turn_left()
            turn_left()
    turn_left()
    turn_left()
"""

if __name__ == "__main__":
    run_karel_program('UpstairsDownstairs.w')
