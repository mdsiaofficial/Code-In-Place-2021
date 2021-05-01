from karel.stanfordkarel import *

"""
File: SafePickup.py
--------------------
When you finish writing this file, Karel should be able to
pick up a beeper from the current position if one is present
(but do nothing if no beepers are present).
"""

def main():
    if beepers_present():   #if any beepers present than, pick
        pick_beeper()


if __name__ == '__main__':
    run_karel_program('SafePickup1.w')