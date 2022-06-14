import math

# A program to calculate the speed of a falling object using the formula:
# v(t) = sqrt(mg/c) * (1-exp((-sqrt(mgc)/m)*t))

# Determine the velocity for a bowling ball, loaf of bread and a skydiver

# Calculate the cross sectional area of a bowling ball
# print("Calculating the cross sectional area of a bowling ball")
# radius = float(input("Radius of bowling ball: "))
# area_ball = math.pi * radius
# print(f"The cross sectional area of a bowling ball is {area_ball:.2f} m^2")
# print()

# Get user input

print("\nWelcome to the velocity calculator. Please enter the following values:")
m = float(input("\nMass in kilograms: "))
print("\nHINT: 9.8m/s^2 on Earth and 24m/s^2 on Jupiter. Only input the value.")
g = float(input("Acceleration due to gravity: "))
t = float(input("\nTime in seconds: "))
print("\nHINT: 1.3kg/m^3 for air and 1000kg/m^3 for water. Only input the value.")
p = float(input("Density of fluid: "))
print("\n0.5 for a sphere, 1.1 for a cylinder falling on it's side. You could look it up for other shapes.")
C = float(input("Drag constant: "))
A = float(input("\nCross sectional area of projectile in square meters: "))
print()


# Perform calculations
# Calculate c
c = (1/2) * p * A * C

# Claculate velocity
velocity = math.sqrt((m * g) / c) * (1 - math.exp((-math.sqrt(m * g * c) / m) * t))

# Print output
print(f"The inner value of c is: {c:.3f}")
print(f"\nThe velocity of the falling object after {t} seconds is: {velocity:.3f} m/s")
option_select = input("\nWould you like to calculate the terminal velocity(Y or N): ").upper()


if option_select == "Y":
    v_terminal = math.sqrt((m * g) / c)
    print(f"The terminal velocity of the object is {v_terminal:.3f} m/s")
elif option_select == "N":
    print("Okay")
else:
    print("Invalid selection. Please try again.")

# time it takes to reach terminal velocity?

# cross sectional area of a human body is 0.001
# drag constant of a skydiver falling feet first is 0.70
# drag constant of a skydiver falling horizantally is 1
