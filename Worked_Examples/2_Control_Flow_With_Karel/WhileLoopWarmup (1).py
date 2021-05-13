from karel.stanfordkarel import *

"""
File: WhileLoopWarmup.py
------------------------------
Clean a spot by picking up beepers until there aren't any left.
"""

def main():
    while beepers_present():
        pick_beeper()

if __name__ == "__main__":
    run_karel_program()
