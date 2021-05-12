"""

"""

def main():
    print("Enter a sequence of non-decreasing numbers.")
    value = input("Enter num: ")

    sequence_length = 0
    while value >= previous_value:
        sequence_length += 1
        previous_value = value

        value = input("Enter num: ")
    print("Thanks for playing!")
    print("Sequence length:", sequence_length)



if __name__ == "__main__":
    main()