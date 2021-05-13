from karel.stanfordkarel import *

"""
File: Max5Karel.py
------------------------------
Karel should place 5 beepers in the bottommost row of the world if the world is more than 5 columns wide.
If the world is less than 5 columns wide, Karel should fill the bottommmost row with beepers and not walk through any walls.
"""

def main():
    for _ in range(5):
        if front_is_clear():
            put_beeper()
            move()

if __name__ == "__main__":
    run_karel_program('Max5Karel1.w')
