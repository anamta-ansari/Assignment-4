# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

def main():
    favourite_animal = input("Enter your favourite animal's name: ")
    print(f"My favourite animal is also {favourite_animal}!")

if __name__ == "__main__":
    main()