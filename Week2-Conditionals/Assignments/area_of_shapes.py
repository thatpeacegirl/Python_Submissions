# Program to calculate the areas of three different shapes

import math

print("Hello! Welcome to our calculator")
print()
print("1.Find the area of a square")
print("2.Find the area of a rectangle")
print("3.Find the area of a circle")
print()
area_option = input("Please select an option from the list: ")

square_length = ""
rec_length = ""
radius = ""
area_cm = ""
rec_width = ""
area_m = ""

if area_option == "1":
    square_length = float(input("Enter the length of a side of the square(cm): "))
    area_cm = square_length ** 2
    area_m = (square_length * 0.01) ** 2
    print(f"The area of the square is {area_cm} cm^2 or {area_m:.2f} m^2")

elif area_option == "2":
    rec_length = float(input("Enter the length of the rectangle(cm): "))
    rec_width = float(input("Enter the width of the rectangle(cm): "))
    area_cm = rec_length * rec_width
    area_m = (rec_length * 0.01) * (rec_width * 0.01)
    print(f"The area of the rectangle is {area_cm} cm^2 or {area_m:.2f} m^2")
    print(f"The area of the rectangle is {(area_cm / 10000):.2f} m^2")

elif area_option == "3":
    radius = float(input("Enter the radius of the circle(cm): "))
    area_cm = math.pi * (radius ** 2)
    area_m = math.pi * (radius * 0.01) ** 2
    print(f"The area of the circle is {area_cm:.2f} cm^2 or {area_m:.2f} m^2")

else:
    print("Invalid operation entered. Please try again")

print()

# A single length value to calculate the areas of 4 shapes

length = float(input("Enter your value: "))

square_area = length ** 2
circle_area = math.pi * (length ** 2)
cube_volume = length ** 3
sphere_volume = (4 / 3) * math.pi * (length ** 3)
print()
print(f"The area of the square is {square_area}")
print(f"The area of the circle is {circle_area:.2f}")
print(f"The volume of the cube is {cube_volume}")
print(f"The volume of the sphere is {sphere_volume:.2f}")