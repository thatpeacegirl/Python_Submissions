# A program to display users full name
# Get users first name
first_name = input("What is your first name? ")

# Get users last name
last_name = input("What is your last name? ")

# Concantenation
full_name = first_name + " " + last_name

# Display output
# Use title in conderation of compound first names and last names
# Using f strings
print(f"Your name is {last_name.title()}, {full_name.title()}.")