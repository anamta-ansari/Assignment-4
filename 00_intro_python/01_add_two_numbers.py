# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

# Prompt the user to enter the first number.

# Read the input and convert it to an integer.

# Prompt the user to enter the second number.

# Read the input and convert it to an integer.

# Calculate the sum of the two numbers.

# Print the total sum with an appropriate message.


def main ():
    print("This program adds two numbers.")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter first number: "))
    sum = num1 + num2
    print("The sum of the two numbers you entered is: ", sum)

if __name__ == '__main__':
    main()    