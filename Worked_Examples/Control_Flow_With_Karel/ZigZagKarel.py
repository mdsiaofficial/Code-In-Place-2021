from karel.stanfordkarel import *

"""
File: ZigZagKarel.py
-----------------------
Places a zig zag pattern of beepers in the world.
"""

def main():
    if front_is_clear():
        zig()
        zag()
        if front_is_blocked():
            put_beeper()
def zig():
    put_beeper()
    move()
    turn_left()
    move()
    turn_right()
def zag():
    put_beeper()
    move()
    turn_right()
    move()
    turn_left()

def zigzag():
    if right_is_clear():
        turn_right()
        move()
    else:
        turn_left()
        move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

if __name__ == "__main__":
    run_karel_program('ZigZag1.w')
