from karel.stanfordkarel import *

"""
File: SteepleChaseKarel.py
--------------------------
Karel runs a steeple chase that is 9 avenues long.
Hurdles are of arbitrary height and placement.
"""

def main ():
	for _ in range(9):
		if front_is_clear():
			move()
		else:
			jump()

# my functions
def turn_right():
	for _ in range(3):
		turn_left()
def move_to_wall():
	while front_is_clear():
		move()
def ascend():
	turn_left()
	while right_is_blocked():
		move()
	turn_right()

def descend():
	turn_right()
	move_to_wall()
	turn_left()
def jump():
	ascend()
	move()
	descend()

if __name__ == '__main__':
  run_karel_program('c:/Users/chester/OneDrive/Documents/Project/Code In Place 2021/Lecture 2/worlds/SteepleChase.w')