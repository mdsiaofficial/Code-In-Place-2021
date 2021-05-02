from karel.stanfordkarel import *

"""
File: LabyrinthKarel.py
------------------------------
Karel solves labyrinths!
"""

def main():
    while front_is_clear():
        move_to_wall()
        find_direction()


def move_to_wall():
    while front_is_clear():
        move()

def find_direction():
    if left_is_clear():
        turn_left()
    else:
        turn_right()

def turn_right():
    for _ in range(3):
        turn_left()
if __name__ == "__main__":
    run_karel_program('Labyrinth1.w')
