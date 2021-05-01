from karel.stanfordkarel import *

"""
File: ExtensionKarel.py
-----------------------
This file is for optional extension programs. 
"""

def main ():
    move()
    move()
    turn_left()
    move()
    turn_around()
    move()
    for i in range(3):
        paint_corner(YELLOW)
        move()
        paint_corner(YELLOW)
    turn_left()
    move()
    turn_around()
    move()
    turn_around()
    paint_corner(YELLOW)
    turn_around()
    move()
    paint_corner(YELLOW)
    for i in range (2):
        move()
        paint_corner(BLACK)
    move()
    paint_corner(BLACK)
    turn_around()
    move()
    turn_left()
    move()
    paint_corner(BLACK)
    move()
    paint_corner(YELLOW)
    turn_around()
    move()
    paint_corner(YELLOW)
    turn_around()
    for i in range(7):
        move()
        paint_corner(YELLOW)
    for i in range(2):
        turn_left()
        move()
    paint_corner(BLACK)
    move()
    paint_corner(BLACK)
    turn_around()
    move()
    turn_around()
    for i in range(2):
        move()
        paint_corner(BLACK)
    turn_around()
    turn_around()
    move()
    move()
    paint_corner(BLACK)
    for i in range(5):
        move()
        paint_corner(BLACK)
    turn_left()
    move()
    paint_corner(YELLOW)
    turn_left()
    for i in range(2):
        move()
        paint_corner(BLACK)
    for i in range(2):
        move()
        paint_corner(YELLOW)
    for i in range(3):
        move()
    paint_corner(YELLOW)
    turn_around()
    for i in range(2):
        move()
    paint_corner(YELLOW)
    turn_around()
    for i in range(5):
        move()
        paint_corner(YELLOW)
    move()
    turn_left()
    move()
    paint_corner(YELLOW)
    for i in range(2):
        move()
    turn_left()
    for i in range(7):
        move()
    turn_left()
    for i in range(7):
        move()
    turn_left()
    move()
    move()
    paint_corner(YELLOW)
    for i in range(5):
        move()
        paint_corner(YELLOW)
    for i in range(1):
        move()
        turn_around()
    move()
    turn_around()
    move()
    for i in range(3):
        move()
        paint_corner(YELLOW)
    move()
    paint_corner(YELLOW)
    for i in range(2):
        move()
    turn_left()
    move()

def turn_around():
    turn_left()
    turn_left()
    turn_left()

if __name__ == '__main__':
  run_karel_program('worlds/41x41.w')