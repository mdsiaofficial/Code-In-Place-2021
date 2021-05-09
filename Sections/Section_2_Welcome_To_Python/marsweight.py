"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""

def main():
    weight_on_earth = int(input("Enter a weight on Earth: "))
    weight_on_mars = (weight_on_earth*37.8)/100
    print("The equivalent on Mars: ", weight_on_mars)

if __name__ == "__main__":
    main()
