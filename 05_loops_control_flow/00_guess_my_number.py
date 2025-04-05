import random

def main():
    random_number = random.randint(0, 99)
    print("I am thinking of a number between 0 and 99")
    
    guess_number = int(input("Enter a guess: "))
    
    while True:
        if guess_number < random_number:
            print("Your guess is too low")
        elif guess_number > random_number:
            print("Your guess is too high")
        else:
            print(f"Congrats! The number was {random_number}")
            break  

        guess_number = int(input("Enter a new guess: "))

if __name__ == "__main__":
    main()
