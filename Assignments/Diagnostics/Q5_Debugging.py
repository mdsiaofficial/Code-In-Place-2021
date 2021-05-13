"""
Part A: It will print the value of n.
Here in this program, n variable is defined twice and in two different function.
One is in the customized funtion user made, and another one in the main function.
So, we know that, a same named variable in different function is totally different in use
So, the program will print the number of m in main function.
"""

"""
Part B: 
Edit this code so that it works correctly
"""

def divide_and_round(n):
    """
    Divides an integer n by 2 and rounds
    up to the nearest whole number
    """
    if n % 2 == 0:
        n = n / 2
        return n
    else:
        n = (n + 1) / 2
        return n
def main():
    n = 10
    n = int(divide_and_round(n))
    print(n)

if __name__ == "__main__":
    main()