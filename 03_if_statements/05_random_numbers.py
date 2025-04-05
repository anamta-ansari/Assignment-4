# Print 10 random numbers in the range 1 to 100.

import random

def main():
    print("Ranndom numbers are: ")
    for _ in range(10):  # Loop 10 times
        random_number = random.randint(1, 100)  # Generate a random number between 1 and 100
        print(random_number, end=" ")  # Print the number with a space

if __name__ == "__main__":
    main()