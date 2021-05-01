from karel.stanfordkarel import *

"""
File: CleanupKarel.py
--------------------
When you finish writing this file, CleanupKarel should be able to
pick up all beepers from the first row of any sized world and
end in the bottom right corner facing East.
"""

def main():
    while front_is_clear():   #if no block in front, move n pick
        if beepers_present():
            pick_beeper()
        move()
    pick_beeper()
    


if __name__ == '__main__':
    run_karel_program('Cleanup1.w')