# A program to display the grade of a student

grade = float(input("What is your score? "))

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

last_digit = grade % 10
# grade_sign = ""
# use this if code isnt running cause of grade_sign outside code block

if last_digit >= 7:
    grade_sign = "+"
elif last_digit < 3:
    grade_sign = "-"
else:
    grade_sign = ""

# Use a place holder since for last_digit from 3-6 have no sign in front of them 

if grade >= 97:
    grade_sign = ""

if letter == "F":
    grade_sign = ""

print(f"Your grade is {letter}{grade_sign}")

if grade >= 70:
    print("Congratulations! You passed the course")
else:
    print("Stay focused. You will pass the course next time!")