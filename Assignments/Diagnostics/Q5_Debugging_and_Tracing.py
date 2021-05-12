def divide_and_round(n):
    """
    Divides an integer n by 2 and rounds
    up to the nearest whole number
    """
    if n % 2 == 0:
        n = n / 2
    else:
        n = (n + 1) / 2

def main():
    n = 10
    divide_and_round(n)
    print(n)  # should print 5

if __name__ == "__main__":
    main()