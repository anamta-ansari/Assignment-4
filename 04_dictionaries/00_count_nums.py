# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

# An example run of the program looks like this (user input is in blue):

# Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.


def main():
    num_counts = {}  # Dictionary to store counts
    
    while True:
        num = input("Enter a number (or press Enter to stop): ")
        if num == "":  # Stop when user presses Enter
            break
        if num.isdigit():  # Check if input is a number
            num = int(num)
            num_counts[num] = num_counts.get(num, 0) + 1  # Update count
        else:
            print("Please enter a valid number.")
    
    print("\nNumber occurrences:")
    for num, count in num_counts.items():
        print(f"{num} appears {count} times.")
    print(f"Dictionary: {num_counts}")

if __name__ == "__main__":
    main()
