# Guess the Number Game 
import random

def main():
    random_number = random.randint(1, 100)
    guess = int(input("Guess number: "))
    while guess != random_number:
        guess = int(input("Enter a new guess: "))
        if guess < random_number:
            print("your guess is too low")
        elif guess > random_number:
            print("your guess is too high")
        elif guess == random_number:
            print(f"Congratulations, you guessed the number! {random_number}")


if __name__ == "__main__":
    main()