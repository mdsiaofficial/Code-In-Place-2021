from karel.stanfordkarel import *

"""
File: WhileLoopWarmup.py
------------------------------
Move Karel forward until you run into a wall (don't walk through the wall!).
"""

def main():
    while front_is_clear():
        move()

if __name__ == "__main__":
    run_karel_program()
