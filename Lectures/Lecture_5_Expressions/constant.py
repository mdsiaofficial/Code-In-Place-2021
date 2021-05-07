"""
constants
An example program with constants that converts feet to inches
"""

#constants define here:
inches_in_foot = 12

def main():
    feet = float(input("Enter number of feet: "))
    inches = feet * inches_in_foot
    print("Here its ", inches, "inches!")


if __name__ == '__main__':
    main()