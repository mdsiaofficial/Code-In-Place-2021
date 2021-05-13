from karel.stanfordkarel import *

"""
File: ForLoopWarmup.py
------------------------------
Put 4 beepers down in a row, starting with Karel's current position.
"""

def main():
    for _ in range(4):
        if front_is_clear():
            put_beeper()
            move()
    put_beeper()

if __name__ == "__main__":
    run_karel_program()
