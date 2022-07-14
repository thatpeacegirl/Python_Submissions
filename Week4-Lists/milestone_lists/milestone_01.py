# A program to ask a user for a series of numbers and
# perform some operations on the numbers.


print("Enter a list of numbers")
print("(Enter 0 when finshed)")
print()

# Declare variables
user_number = -1
number_sum = 0
number_list = []
positive_number_list = []

# Loop the program as long as user input is not 0
while user_number != 0:

    # Get user input
    user_number = int(input("Enter a number: "))

    # Done to ensure that the user input 0 is not added to the list
    if user_number != 0:

        # Add each user input to the end of the list
        number_list.append(user_number)

# Loop through the shopping list and add the numbers in the list together
for number in number_list:
    number_sum += number

    # Add all positive numbers to another list
    if number > 0:
        positive_number_list.append(number)

# Perform calculations
# Sort the lists in ascending order
number_average = number_sum / len(number_list)
number_list.sort()
positive_number_list.sort()

# Print out the desired outputs
print()
print(f"The sum is: {number_sum}")
print(f"The average is: {number_average}")
print(f"The largest number is: {number_list[-1]}")
print(f"The smallest positive number is: {positive_number_list[0]}")
print("\nThe sorted list is:")

# Print out the sorted list
for number in number_list:
    print(number)