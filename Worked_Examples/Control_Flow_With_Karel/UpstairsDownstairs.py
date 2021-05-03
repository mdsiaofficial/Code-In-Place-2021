from karel.stanfordkarel import *

"""
File: UpstairsDownstairs.py
------------------------------
Karel will climb three stair steps up and then three stair steps down.
"""

def main():
    climb_mountain()



def climb_mountain():
    while front_is_blocked():
        step_up()
        step_up()

def step_up():
    # karel must be facing east
    turn_left()
    move()
    turn_right()
    move()


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
