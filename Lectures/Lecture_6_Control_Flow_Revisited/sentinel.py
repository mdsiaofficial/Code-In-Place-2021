"""
Asks the user for a number until they enter -1
Reports the total value of all the numbers at the end
"""

sentinel = int(-1)

def main():
    num = int(input("Type a number: "))
    total = 0
    while num != sentinel:
        total = total + num
        num = int(input("Type a number: "))


    print("Total is " + str(total))
if __name__ == '__main__':
    main()
