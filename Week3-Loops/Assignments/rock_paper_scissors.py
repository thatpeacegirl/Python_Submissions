import random
import time

option_list = ["R", "P", "S"]
user_name = input("\nEnter your name: ").capitalize()
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
while game_play == "y":

    computer_choice = random.choice(option_list)
    user_choice = input("\nSelect an option(R, P or S): ").upper()
    print()

    if user_choice not in option_list:
        print("Invalid input. Please try again")
        continue

    print(user_name, "chose", user_choice )
    print("The computer is making a choice...")
    print()
    time.sleep(2)
    print("The computer chose", computer_choice)
    print()

    if user_choice == computer_choice:
        print("It's a tie!")
        continue

    elif user_choice == "R":
        if computer_choice == "P":
            print(f"Paper covers rock. {user_name} loses")
        else:
            print(f"Rock smashes scissors. {user_name} wins!")

    elif user_choice == "P":
        if computer_choice == "S":
            print(f"Scissors cuts paper. {user_name} loses")
        else:
            print(f"Paper covers rock. {user_name} wins!")

    elif user_choice == "S":
        if computer_choice == "R":
            print(f"Rock smashes scissors. {user_name} loses")
        else:
            print(f"Scissors cuts paper. {user_name} wins!")

    game_play = input("Do you want to play again? (Y/N) ").lower()

print("\nThank you for playing")



# Submission Comment
# This game program satisfies the core requirements of the assignment.