from karel.stanfordkarel import *

"""
File: WhileLoopWarmup.py
------------------------------
Turn left until Karel is facing a wall.
"""

def main():
    while front_is_clear():
        turn_left()

if __name__ == "__main__":
    run_karel_program()
