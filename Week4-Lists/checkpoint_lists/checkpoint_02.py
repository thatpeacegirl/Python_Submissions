# A program to ask the user for a list of items in a shopping list,
# then print the list items with their indexes


print()
print("Please enter the items of the shopping list")
print("(Enter quit to finish)")
print()

# Declare variables
list_item = ""
shopping_list = []

# Loop the program as long as user input is not "Quit"
while list_item != "Quit":
    
    # Get user input
    list_item = input("Item: ").capitalize()
    
    # Done to ensure that the user input "Quit" is not added to the list
    if list_item != "Quit":

        # Add each user input to the end of the list
        shopping_list.append(list_item)

print("\nThe shopping list is:")

# Loop through the shopping list and print out each item
for i in shopping_list:
    print(i)

print("\nThe shopping list with indexes is:")

# Loop through the shopping list and print out each item with its index
for i in range(len(shopping_list)):
    item = shopping_list[i]
    print(f"{i}. {item}")

# Replacing an item in the shopping list
# Get user input
new_item_index = int(input("\nWhich item would you like to change(the number)? "))
new_item = input("What is the new item? ")
print()

# Remove user item at a particular index
shopping_list.pop(new_item_index)
# Add a new item at the same index
shopping_list.insert(new_item_index, new_item)

print("\nThe shopping list with indexes is:")

# Loop through the new shopping list and print out each item with its index
for i in range(len(shopping_list)):
    item = shopping_list[i]
    print(f"{i}. {item}")