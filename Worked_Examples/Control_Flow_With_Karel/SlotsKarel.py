from karel.stanfordkarel import *

"""
File: SlotsKarel.py
-----------------------
Place 10 beepers in all spots on the bottom row of any sized world.
"""

def main():
    turn_right()
    move()
    turn_left()
    if front_is_blocked():
        put_beeper()
        turn_left()
        move()
        turn_right()
    move()
    turn_right()
    move()
    put_beeper()
    turn_left()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    put_beeper()
    turn_left()
    turn_left()
    move()
    turn_right()
def turn_right():
    for _ in range(3):
        turn_left()

if __name__ == "__main__":
    run_karel_program('Slots.w')
