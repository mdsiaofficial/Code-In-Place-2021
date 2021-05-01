from karel.stanfordkarel import *

"""
File: IfElseWarmup.py
------------------------------
If Karel is facing a wall, put a beeper down, turn left, and move forward. If not, do nothing.
"""

def main():
    if front_is_blocked():
        turn_left()
        put_beeper()


if __name__ == "__main__":
    run_karel_program('FrontBlocked.w')
