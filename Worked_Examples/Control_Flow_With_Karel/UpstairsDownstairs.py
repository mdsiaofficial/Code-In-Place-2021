from karel.stanfordkarel import *

"""
File: UpstairsDownstairs.py
------------------------------
Karel will climb three stair steps up and then three stair steps down.
"""

def main():
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
        while front_is_clear():
            move()
        if front_is_blocked():
            turn_left()
            turn_left()
            turn_left()
    turn_left()
    turn_left()
if __name__ == "__main__":
    run_karel_program('UpstairsDownstairs.w')
