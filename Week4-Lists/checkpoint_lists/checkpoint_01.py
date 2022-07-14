# A program to ask a user for the names of their friends and append
# them to a list and then displays each of their friends in the list.

# Declare variables
friends = []
user_friend = ""

# Loop the program as long as user input is not "End"
while user_friend != "End":
    
    # Get user input
    user_friend = input("Enter the name of a friend: ").capitalize()
    
    # Done to ensure that the user input "End" is not added to the list
    if user_friend != "End":

        # Add each user input to the end of the list
        friends.append(user_friend)

print("\nYour friends are: ")

# Loop through the friend list and print out each name
for friend in friends:
    print(friend)