# A program to calculate the areas of three different shapes

import math

# Display user options
print("Hello! Welcome to our calculator")
print()
print("1.Find the area of a square")
print("2.Find the area of a rectangle")
print("3.Find the area of a circle")
print()

# Get user input for their choice
area_option = input("Please select an option from the list: ")

# Calculating the area of a square
if area_option == "1":
    # Get user input for the length of a side of the square in cm
    square_length = float(input("Enter the length of a side of the square(cm): "))
    # Perform calculations
    area_cm = square_length ** 2
    area_m = (square_length * 0.01) ** 2
    # Display the calculation results
    print(f"The area of the square is {area_cm} cm^2 or {area_m:.2f} m^2")

# Calculating the area of a rectangle
elif area_option == "2":
    # Get user input for the length and width of the rectangle in cm
    rec_length = float(input("Enter the length of the rectangle(cm): "))
    rec_width = float(input("Enter the width of the rectangle(cm): "))
    # Perform calculations
    area_cm = rec_length * rec_width
    area_m = (rec_length * 0.01) * (rec_width * 0.01)
    # Display the calculation results
    print(f"The area of the rectangle is {area_cm} cm^2 or {area_m:.2f} m^2")
    print(f"The area of the rectangle is {(area_cm / 10000):.2f} m^2")

# Calculating the area of a circle
elif area_option == "3":
    # Get user input for the radiius of the circle in cm
    radius = float(input("Enter the radius of the circle(cm): "))
    # Perform calculations
    area_cm = math.pi * (radius ** 2)
    area_m = math.pi * (radius * 0.01) ** 2
    # Display the calculation results
    print(f"The area of the circle is {area_cm:.2f} cm^2 or {area_m:.2f} m^2")

# Invalid user input
else:
    print("Invalid operation entered. Please try again")

print()



# A single length value to calculate the areas of 4 shapes

# Get user input
length = float(input("Enter your value: "))

# Perform calculations
square_area = length ** 2
circle_area = math.pi * (length ** 2)
cube_volume = length ** 3
sphere_volume = (4 / 3) * math.pi * (length ** 3)
print()

# Display the calculation results
print(f"The area of the square is {square_area}")
print(f"The area of the circle is {circle_area:.2f}")
print(f"The volume of the cube is {cube_volume}")
print(f"The volume of the sphere is {sphere_volume:.2f}")