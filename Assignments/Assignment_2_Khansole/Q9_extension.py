"""
Hailstones
A separate (optional) problem you could consider writing is based on a problem in Douglas Hofstadter’s Pulitzer-prize-winning book Gödel, Escher, Bach. That book contains many interesting mathematical puzzles, many of which can be expressed in the form of computer programs. In Chapter XII, Hofstadter mentions a wonderful problem that is well within the scope of what you know. The problem can be expressed as follows:

Pick some positive integer and call it n.
If n is even, divide it by two.
If n is odd, multiply it by three and add one.
Continue this process until n is equal to one.
"""

def main():
    user_input = int(input("Enter a number: "))

    while user_input != 1
        if user_input % 2 == 0:
            n1 = user_input // 2
            print(user_input, "is even, so I take half: ", n1)
            user_input = n1
        else:
            n2 = (user_input*3)+1
            print(user_input, "is odd, so I make 3n+1: ", n2)
            user_input = n2


if __name__ == "__main__":
    main()
