from karel.stanfordkarel import *

"""
File: ForLoopWarmup.py
------------------------------
Get Karel to do a cool backflip by turning left 4 times.
"""

def main():
    Backflip()

def Backflip():
    for _ in range(4):
        turn_left()

if __name__ == "__main__":
    run_karel_program()
