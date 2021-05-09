"""
Prints out 10 random numbers between 0 and 100.
"""

import random

def main():
    for _ in range(10):
        print(random.randint(0,100))

if __name__ == '__main__':
    main()
