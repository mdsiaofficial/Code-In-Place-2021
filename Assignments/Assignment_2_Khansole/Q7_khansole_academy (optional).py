"""
TODO: Write a description here
"""

import random

def main():
    correct_count=0
    while True:
        num1 = random.randint(10,99)
        num2 = random.randint(10,99)
        sum = num1+num2
        print("What is "+str(num1)+"+"+str(num2)+"?")
        user_input = int(input("Your answer: "))
        if user_input==sum:
            correct_count += 1
            print("Correct! You've gotten ",correct_count, "correct in a row.")
        else:
            print("Incorrect. The expected answer is ",sum)

        if correct_count==3:
            print("Congratulations! You mastered addition.")
            break

if __name__ == '__main__':
    main()
