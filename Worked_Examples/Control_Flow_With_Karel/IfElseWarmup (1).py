from karel.stanfordkarel import *

"""
File: IfElseWarmup.py
------------------------------
Turn based on whether or not a beeper is present.
"""

def main():
    if beepers_present():
        turn_left()
    else:
        for _ in range(3):
            turn_left()



if __name__ == "__main__":
    run_karel_program('1x1Beeper.w')
