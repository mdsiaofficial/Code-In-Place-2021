from karel.stanfordkarel import *

"""
File: StepUp.py
--------------------
Karel should pick up the beeper and put it on the ledge
"""

def main():
    move()
    pick_beeper()
    move()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    put_beeper()
    move()

if __name__ == "__main__":
    run_karel_program('StepUp.w')
