"""
Another python program to get some practice with variables.
This program asks the user for two integers and prints their sum.
"""

def main():
    x = input('Gimme your first number: ')
    y = input('Gimme your second number: ')
    add2numbers = int(x)+int(y)
    print(add2numbers)
# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
