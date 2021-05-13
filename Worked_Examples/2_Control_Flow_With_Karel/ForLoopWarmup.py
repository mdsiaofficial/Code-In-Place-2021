from karel.stanfordkarel import *

"""
File: ForLoopWarmup.py
------------------------------
Place 10 beepers.
"""

def main():
    for _ in range(10):
        put_beeper()

if __name__ == "__main__":
    run_karel_program()
