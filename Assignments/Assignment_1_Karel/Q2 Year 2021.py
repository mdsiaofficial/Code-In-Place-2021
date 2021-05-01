from karel.stanfordkarel import *

"""
File: 2021.py
--------------------
When you finish writing this file, Karel should be able to place 20 beepers,
then 21 beepers, and end facing East to the right of the 21 beepers.
"""

def main():
    for _ in range(20):    #using loop to put_beeper for 20 times
        put_beeper()
    move()
    for _ in range(21):      #using loop to put_beeper for 21 times
        put_beeper()
    move()

if __name__ == '__main__':
    run_karel_program('3x3.w')