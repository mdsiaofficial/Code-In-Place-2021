from karel.stanfordkarel import *

"""
File: ClimbStem.py
------------------------------
Karel will climb a "stem" -- Karel should start facing a wall. Karel will turn and scale the wall until there is no more wall to Karel's right.
"""

def main():
    if front_is_clear():
        move()
    else:
        turn_left()
        
    while right_is_blocked():
        move()

if __name__ == "__main__":
    run_karel_program()
