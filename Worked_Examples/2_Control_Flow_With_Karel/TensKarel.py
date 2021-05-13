from karel.stanfordkarel import *

"""
File: TensKarel.py
-----------------------
Place 10 beepers in all spots on the bottom row of any sized world.
"""

def main():
    while front_is_clear():
        put_beeper()
        move()
    if front_is_blocked():
        put_beeper()

if __name__ == "__main__":
    run_karel_program('TensKarel1.w')
