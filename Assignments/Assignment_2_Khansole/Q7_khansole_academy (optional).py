"""
TODO: Write a description here
"""

import random
cmplt_prgrm = 3
def main():

    num1 = random.randint(10,99)
    num2 = random.randint(10,99)
    sum = num1+num2
    print("What is "+str(num1)+"+"+str(num2)+"?")
    user_input = int(input("Your answer: "))
    if user_input==sum:
        print("Correct!")
    else:
        print("Incorrect. The expected answer is "+str(sum))

if __name__ == '__main__':
    main()
