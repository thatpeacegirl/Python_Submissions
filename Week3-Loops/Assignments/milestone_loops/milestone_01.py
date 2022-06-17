# Guess my number game

# In the Guess My Number game the computer picks a magic number, and then 
# the user tries to guess it. After each guess, the computer tells the user
# to guess "higher" or "lower" until they guess the magic number.

import random


magic_number = random.randint(1, 100)

guess_count = 0
game_play = "y"
print()

while game_play == "y":

    guess_number = int(input("What is your guess? "))
    guess_count += 1

    if guess_number < magic_number:
        print("Higher")
    elif guess_number > magic_number:
        print("Lower")
    else:
        print("\nYou guessed it!")
        print(f"The number of guesses is: {guess_count}")

        game_play = input("\nDo you want to play again?(Y/N) ").lower()

        if game_play == "y":
            guess_count = 0
            magic_number = random.randint(1, 100)
            print()
            continue
else:
    print("Thank you for playing!")


    

# Is there a better way to write the if game_play == "y" condition 
# without repeating the magic_number variable and the guess_count = 0 ?