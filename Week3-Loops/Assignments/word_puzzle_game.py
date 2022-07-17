# An interactive word puzzle game that allows the user to guess 
# a secret hidden word and make guesses until they get the answer 
# correct, and hints are provided along the way.

# Import modules
import random

# Set a list of words to choose from to guess
word_list = ["angry", "kingdom", "controller", "phoenix", "serene"]

# Display message
print("\nWelcome to the word guessing game!")
print("""
RULES
- An uppercase letter shows that the letter is at the correct \
position in the secret word.
- A lowercase letter shows that the letter is in the secret word \
but not at the correct position.
- An underscore shows that the letter isn't present in the secret word.
""")

# Declare game_play variable
game_play = "y"

# Loop as long as user types "y" to play the game
while game_play == "y":

    # Declare other variables
    secret_word = random.choice(word_list)
    user_guess = ""
    guess_count = 0

    # Give the user a hint to show the number of letters to guess
    print("Your hint is: ", end="")

    # Loop to show the number of letters in the secret word
    for hint in secret_word:
        print("_ " , end="")
    print()

    # Loop to run as long as the user has not guessed the secret word
    while user_guess != secret_word:
        user_guess = input("What is your guess? ").lower()
        # Count the number of guesses the user makes
        guess_count += 1

        # Conditional to run once the user guesses the secret word
        if user_guess == secret_word:
            print("\nCongratulations! You guessed the secret word")
            print(f"Your guess count is: {guess_count}")
            break
        # Conditional to run when the user did not guess the secret word
        else:
            # Count the number of letters in the users guess
            for i in range(len(user_guess)):
                # Use index of user guess to determine how the next hint will be displayed
                guess_letter = user_guess[i]
            
                # Display uppercase letter if the guessed letter
                # is in the same position in the secret word
                if guess_letter == secret_word[i]:
                    print(guess_letter.upper(), end="")

                # Display lowercase letter if the guessed letter
                # is in the secret word but not in the correct position
                elif guess_letter in secret_word:
                    print(guess_letter.lower(), end="")

                # Display an underscore if the guessed letter
                # is not in the secret word
                else:
                    print("_ ", end="")
            print()

    # Get user input if they want to play again
    game_play = input("\nDo you want to play again?(Y/N) ").lower()
    print()

print("Thank you for playing!")


# Preventing IndexError when the user guess is lesser/greater than the secret word?