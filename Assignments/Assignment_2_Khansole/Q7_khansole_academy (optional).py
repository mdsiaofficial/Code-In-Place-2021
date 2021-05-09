"""
TODO: Write a description here
"""

import random
cmplt_prgrm = 3


def main():

    num1 = random.randint(10,99)
    num2 = random.randint(10,99)
    sum = num1+num2
    correct_count = 0
    print("What is "+str(num1)+"+"+str(num2)+"?")
    user_input = int(input("Your answer: "))

    while correct_count !=cmplt_prgrm:
        if user_input==sum and correct_count<cmplt_prgrm:
            print("Correct!")
            correct_count+=1
            print("What is " + str(num1) + "+" + str(num2) + "?")
            user_input = int(input("Your answer: "))
        else:
            print("Incorrect. The expected answer is "+str(sum))
            print("What is " + str(num1) + "+" + str(num2) + "?")
            user_input = int(input("Your answer: "))
    print(Correct! You've gotten 3 correct in a row.')
    print("Congratulations! You mastered addition.")
if __name__ == '__main__':
    main()
