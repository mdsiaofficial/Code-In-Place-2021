"""
Asks the user for two numbers and prints the result
of the first number minus the second number.
"""

def main():
    print("This program subtracts one number from another.")
    user_input1 = float(input("Enter first number: "))
    user_input2 = float(input("Enter second number: "))
    print("The result is "+user_input1-user_input2)
if __name__ == '__main__':
    main()
