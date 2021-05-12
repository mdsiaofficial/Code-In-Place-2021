"""
Write a program that asks the user to enter a sequence of "non-decreasing" numbers one at a time. Numbers are non-decreasing if each number is greater than or equal to the last.

When the user enters a number which is smaller than their previously entered value, the program is over. Tell the user how long their sequence was.

Here is an example (values entered by the user are bolded and italicized for clarity, but they don't need to be in your program):
"""

def main():

    print("Enter a sequence of non-decreasing numbers.")
    value = input("Enter num: ")
    # here its defining the prev of main value
    previous_value = value
    sequence_length = 0     # its steps need to do
    while value >= previous_value:
        sequence_length += 1
        previous_value = value
        value = input("Enter num: ")
    print("Thanks for playing!")
    print("Sequence length:", sequence_length)



if __name__ == "__main__":
    main()