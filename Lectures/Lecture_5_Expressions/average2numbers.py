"""
average2numbers
This program asks the user for two numbers and prints their average.
"""

def main():
    first_number = float(input('Gimme 1st number: '))
    second_number = float(input('Gimme 2nd number: '))
    average = (first_number+second_number)/2
    print(average)

if __name__ == '__main__':
    main()