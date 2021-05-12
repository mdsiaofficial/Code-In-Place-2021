"""
Write a program which asks the user for their height in meters and prints whether or not they are the correct height to be a NASA astronaut.

If their height is between 1.6 meters and 1.9 meters, print "Correct height to be an astronaut".

If their height is less than 1.6 meters, print "Below minimum astronaut height".

If their height is greater than 1.9 meters, print "Above maximum astronaut height".

Here are a few examples. User input is bolded and italicized for clarity, but it doesn't need to be in your program:
"""
def main():
    min_height = 1.6
    max_height = 1.9
    height = float(input("Enter your height in meters: "))
    if height >= min_height and height <=max_height:
        print("Correct height to be an astronaut")
    elif height > max_height:
        print("Above maximum astronaut height")
    else:
        print("Below minimum astronaut height")

if __name__ == '__main__':
    main()