# A program to display the grade of a student

# Get user input
grade = float(input("What is your score? "))

# Check the value of user grade to determine grade letter
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

# Check the last digit of the user grade to determine the appropriate sign
last_digit = grade % 10

if last_digit >= 7:
    grade_sign = "+"
elif last_digit < 3:
    grade_sign = "-"
else:
    grade_sign = ""

# Condition for grades that do not require a grade sign
if grade >= 97:
    grade_sign = ""

if letter == "F":
    grade_sign = ""

# Display grade with the corresponding sign
print(f"Your grade is {letter}{grade_sign}")

# Congratulatory messages to be displayed based on conditions
if grade >= 70:
    print("Congratulations! You passed the course")
else:
    print("Stay focused. You will pass the course next time!")