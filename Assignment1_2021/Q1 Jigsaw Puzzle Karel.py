from karel.stanfordkarel import *

"""
File: PuzzleKarel.py
--------------------
Karel should finish the puzzle by picking up the last beeper (puzzle piece) and placing it in the right spot.
Karel should end in the same position Karel starts in -- the bottom left corner of the world.
"""

def main():
    move()
    move()
    pick_beeper()
    move()
    turn_left()
    move()
    move()
    put_beeper()
    turn_left()
    turn_left()
    move()
    move() 
    turn_right() #using turn_right function i created
    move()
    move()
    move()
    turn_left()
    turn_left()

def turn_right(): #it defines turn_right function
    for _ in range(3):
        turn_left()


if __name__ == '__main__':
    run_karel_program('Puzzle.w')