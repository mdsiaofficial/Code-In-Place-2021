"""
average2numbers
This program asks the user for two numbers and prints their average.
"""

def main():
    first_number = input('Gimme 1st number: ')
    second_number = input('Gimme 2nd number: ')
    average = (int(first_number)+int(second_number))/2
    print('Your Average is: ' + float(average))

if __name__ == '__main__':
    main()