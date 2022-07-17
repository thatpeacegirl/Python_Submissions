# A program to track bank accounts and the balances in each account

# Display a message
print("Enter the names and balances of bank accounts")
print("(Enter quit in account name when done)\n")

# Declare variables
account_names = []
account_balances = []
user_account = ""
total_balance = 0

# Loop the program as long as user input is not "Quit"
while user_account != "Quit":

    # Get user input
    user_account = input("What is the name of this account? ").capitalize()

    # Done to ensure that the user input "Quit" is not added to the list
    if user_account != "Quit":

        # Get user input
        user_balance = float(input("What is the current balance of the account? "))
        # Add each user input to the end of the lists
        account_names.append(user_account)
        account_balances.append(user_balance)

print("\nAccount Information:")

# Print out the desired output using the index of items in a list
for i in range(len(account_names)):
    name = account_names[i]
    balance = account_balances[i]
    print(f"{i}. {name} - ${balance}")

    # Add all the items in the account_balances list together
    total_balance += balance

# Perform calculations and sort the list
balance_average = total_balance / len(account_balances)
balances_sorted = sorted(account_balances)

# Print out the desired outputs
print()
print(f"Total: ${total_balance:.2f}")
print(f"Average: ${balance_average:.2f}")
print(f"Highest balance: ${balances_sorted[-1]:.2f}")


update_account = "Y"

# Loop the program as long as user input is not "Y"
while update_account == "Y":

    # Get user input
    update_account = input("\nDo you want to update an account?(Y/N) ").capitalize()

    # Conditional to run if user input is "Y"
    if update_account == "Y":

        # Get user input
        index_update_account = int(input("What account index do you want to update? "))
        new_amount = float(input("What is the new amount? "))
        # Remove user item at a particular index
        account_balances.pop(index_update_account)
        # Add a new item at the same index
        account_balances.insert(index_update_account, new_amount)

        print("\nAccount Information:")

        # Print out the desired output using the index of items in a list
        for j in range(len(account_names)):
            name = account_names[j]
            balance = account_balances[j]
            print(f"{j}. {name} - ${balance}")



# Note: Highest balance doesn't include the account name