# Ask the user for a number and print its square (the product of the number times itself).

def square():
    num = int(input("Enter a number to see its square: "))
    square = num * num 
    print(f"The square of {num} is {square}.")

if __name__ == "__main__":
    square()