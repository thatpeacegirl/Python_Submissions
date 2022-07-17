# A Rock-Paper-Scissors game with two players. One player is controlled by 
# the computer and the other player is controlled by you(the user)

# Import modules
import random
import time

# Set the list of options
option_list = ["R", "P", "S"]
# Get user input
user_name = input("\nEnter your name: ").capitalize()
# Display a message
print("\nLet's play Rock, Paper, Scissors!")
print()
time.sleep(2)
print("Rock(R)")
time.sleep(1)
print("Paper(P)")
time.sleep(1)
print("Scissors(S)")
time.sleep(1)
print("Shoot!")

game_play = "y"
# Loop as long as user types "y" to play the game
while game_play == "y":

    # Computer selects a choice from the list of options
    computer_choice = random.choice(option_list)
    # Get user choice
    user_choice = input("\nSelect an option(R, P or S): ").upper()
    print()

    # Condition if user choice is not in the list of possible choices
    if user_choice not in option_list:
        print("Invalid input. Please try again")
        continue

    # Display a message
    print(user_name, "chose", user_choice )
    print("The computer is making a choice...")
    print()
    time.sleep(2)
    print("The computer chose", computer_choice)
    print()

    # User choice and computer choice are the same thing
    if user_choice == computer_choice:
        print("It's a tie!")
        continue

    # User choice is "R"
    elif user_choice == "R":
        # Computer choice is "P"
        if computer_choice == "P":
            print(f"Paper covers rock. {user_name} loses")
        # Computer choice is "S"
        else:
            print(f"Rock smashes scissors. {user_name} wins!")

    # User choice is "P"
    elif user_choice == "P":
        # Computer choice is "S"
        if computer_choice == "S":
            print(f"Scissors cuts paper. {user_name} loses")
        # Computer choice is "R"
        else:
            print(f"Paper covers rock. {user_name} wins!")

    # User choice is "S"
    elif user_choice == "S":
        # Computer choice is "R"
        if computer_choice == "R":
            print(f"Rock smashes scissors. {user_name} loses")
        # Computer choice is "P"
        else:
            print(f"Scissors cuts paper. {user_name} wins!")

    # Ask user if they want to play again
    game_play = input("Do you want to play again? (Y/N) ").lower()

# Goodbye message
print("\nThank you for playing")