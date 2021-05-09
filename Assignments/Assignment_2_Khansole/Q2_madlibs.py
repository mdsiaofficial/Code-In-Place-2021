"""
Uses constants to tell a mad libs story.
"""

# Fun fact: 6174 is known as Kaprekar's constant,
# and it's a pretty mysterious number :)

WIZARD = 'Karel the Omniscient'
NUMBER_OF = 6174
FRUIT = 'mangoes'
PRICE = 2.99
YEARS = 300

def main():
    print("There once was a wizard by the name of " + WIZARD + " who loved to eat " + FRUIT + ".")
    print(WIZARD + " always kept a stash of " + str(NUMBER_OF) + " " + FRUIT + " in their mini fridge!")
    print(WIZARD + " realized they couldn't keep all those " + FRUIT + " to themselves,")
    print("so they sold them at the market for $" + str(PRICE) + " apiece,")
    print("and with the earnings bought fruit to share with the entire village!")

if __name__ == '__main__':
    main()
