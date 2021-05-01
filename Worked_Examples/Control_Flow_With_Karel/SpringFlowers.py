from karel.stanfordkarel import *

"""
File: SpringFlowers.py
------------------------------
Karel starts in the bottom left corner of a world with 2 empty flower stems, facing East.
Karel should bloom both flowers with beepers and end in the bottom right corner of the world facing East.
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
    run_karel_program('SpringFlowers1.w')
