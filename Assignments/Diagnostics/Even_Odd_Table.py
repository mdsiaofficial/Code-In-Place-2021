"""
Print out each of the numbers 1 through 100 and whether that number is even or odd.

100 is specified using a constant MAX_NUMBER.

Here is what the output looks like when MAX_NUMBER = 100
"""


MAX_NUMBER = 100
MIN_NUMBER = 1
def main():
    while MIN_NUMBER <= 100:
        if MIN_NUMBER % 2 == 0:
            print(i, "is even")
        else:
            print(i, "is odd")
        MIN_NUMBER += 1

if __name__ == '__main__':
    main()