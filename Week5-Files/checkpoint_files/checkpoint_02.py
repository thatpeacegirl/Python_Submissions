# A program to find the youngest person in a list


# Declare variables
people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
young_age = 60   # Value is greater than list item

# Iterate through each item in the list
for i in people:
    # Split the item using a whitespace
    items = i.split(" ")
    # Assign the split items to a variable using their indexes
    name = items[0]
    age = int(items[1])
    # Conditional if the age is less than the youngest person's age
    if age < young_age:
        young_age = age
        youngest_person = name

# Print a set of statements to the screen        
print(f"The youngest person is {young_age} years old")
print(f"The name of the youngest person is: {youngest_person}")