from karel.stanfordkarel import *

"""
File: ExtensionKarel.py
-----------------------
This file is for optional extension programs. 
"""

def main ():
    while front_is_clear():
        put_beeper()
        move()
    if beepers_present():
            move()

    put_beeper()
def turn_right():
    for _ in range(3):
        turn_left()
if __name__ == '__main__':
  run_karel_program('worlds/SteepleChase.w')