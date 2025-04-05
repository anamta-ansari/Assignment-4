# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

import random

NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    total: int = die1 + die2 
    print("Total of two dice:", total)

def main():
    print("Rolling dice three times")
    roll_dice()
    roll_dice()
    roll_dice()


if __name__ == '__main__':
    main()
