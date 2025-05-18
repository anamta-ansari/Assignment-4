# Rock paper scissors

import random


def main():
    player = input("'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r','p', 's'])
    if player == computer:
        print(f"Player and computer both chose {player}. It's a tie!")
    elif (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
        print(f"Player chose {player}, computer chose {computer}. you wins!")
    else:
        print(f"Player chose {player}, computer chose {computer}. you lost!")

if __name__ == "__main__":
    main()