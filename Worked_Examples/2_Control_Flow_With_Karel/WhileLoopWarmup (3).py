from karel.stanfordkarel import *

"""
File: WhileLoopWarmup.py
------------------------------
Fill the entire bottom row of the world with beepers.
"""

def main():
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()
    put_beeper()

if __name__ == "__main__":
    run_karel_program()
