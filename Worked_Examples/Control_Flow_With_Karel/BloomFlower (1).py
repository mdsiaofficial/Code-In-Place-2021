from karel.stanfordkarel import *

"""
File: BloomFlower.py
------------------------------
Karel will scale the stem of the flower she's facing, bloom the flower with 4 beepers, and return to the ground.
Karel should end up in the bottommost row, directly to the right of the stem, facing East.
"""

def main():
    if front_is_clear():
        move()
    else:
        turn_left()
        
    while right_is_blocked():
        move()
    bloom_flower()

    move_to_wall()
    turn_left()
    move_to_wall()

    if front_is_clear():
        move()
    else:
        turn_left()
        
    while right_is_blocked():
        move()
    bloom_flower()


def bloom_flower():
    put_beeper()
    move()
    put_beeper()
    turn_right()
    move()
    put_beeper()
    turn_right()
    move()
    put_beeper()
def move_to_wall():
    while front_is_clear():
        move()
def turn_right():
    for _ in range(3):
        turn_left()

if __name__ == "__main__":
    run_karel_program()
