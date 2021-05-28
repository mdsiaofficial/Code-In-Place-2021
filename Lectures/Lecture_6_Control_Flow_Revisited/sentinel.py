"""
Asks the user for a number until they enter -1
Reports the total value of all the numbers at the end
"""

sentinel = -1

def main():
    num = input("Type a number: ")

    while num != sentinel:
        num = input("Type a number: ")

if __name__ == '__main__':
    main()
