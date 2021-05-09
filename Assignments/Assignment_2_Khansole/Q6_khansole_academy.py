"""
Prints out a randomly generated addition problem
and checks if the user answers correctly.
"""

import random 

def main():
    num1 = random.randint(10,99)
    num2 = random.randint(10,99)
    sum = num1+num2

    print(sum)

if __name__ == '__main__':
    main()
