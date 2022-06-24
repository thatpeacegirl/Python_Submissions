# Guess my number game

# In the Guess My Number game the computer picks a magic number, and then 
# the user tries to guess it. After each guess, the computer tells the user
# to guess "higher" or "lower" until they guess the magic number.

import random

game_play = "y"
while game_play == "y":
    
    magic_number = random.randint(1, 100)
    guess_number = -1    #This number will not be easily guessed and it can also be 0
    guess_count = 0
    print()

    while guess_number != magic_number :

        guess_number = int(input("What is your guess? "))
        guess_count += 1

        if guess_number < magic_number:
            print("Higher")
        elif guess_number > magic_number:
            print("Lower")
        else:
            print("\nYou guessed it!")

    print()   
    print(f"The number of guesses is: {guess_count}")

    game_play = input("\nDo you want to play again?(Y/N) ").lower()
    # if game_play == "y":
    #     break
    
print("Thank you for playing!")