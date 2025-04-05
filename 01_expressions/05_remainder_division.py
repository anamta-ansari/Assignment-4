# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

def main():
    num1 = int(input("Enter an integer to be divided: "))
    num2 = int(input("Enter an integer to divide by: "))
    division = int(num1 / num2)
    remainder = num1 % num2
    print(f"The result of the division is {division} with remainder of {remainder}")


if __name__ == "__main__":
    main()