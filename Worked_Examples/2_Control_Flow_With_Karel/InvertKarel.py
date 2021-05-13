from karel.stanfordkarel import *

"""
File: InvertKarel.py
-----------------------
Inverts the pattern of beepers in a single row world.
"""

def main():
    while front_is_clear():
        if beepers_present():
            pick_beeper()
            move()
        else:
            put_beeper()
            move()
        if front_is_blocked():
            if beepers_present():
                pick_beeper()
            else:
                put_beeper()



if __name__ == "__main__":
    run_karel_program('Invert1.w')
