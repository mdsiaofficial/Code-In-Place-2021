"""
dicesimulator
This program simulates rolling two dice, three times. It prints the results of each die roll.

This program is used to show how variable scope works.
"""

#import here
import random
def main():
    die1 = 10
    print("die1 in main() starts as: " + str(die1))

if __name__ == '__main__':
    main()