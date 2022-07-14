# A Program to help an amusement park ride attendant know if a ride is allowed to go

print("\nIs a prospective rider acceptable to ride or not?\n")

can_ride = False

age_one = int(input("What is the age of the first rider? "))
height_one = int(input("What is the height of the first rider? "))

# A single rider with golden passport
if age_one in range (12,18):
    golden_passport1 = input("Do you have a golden passport?(Y/N) ").lower()

# Ask for a second rider
rider_prompt = input("\nIs there a second rider?(Y/N) ").lower()
print()

# Case for two riders
if rider_prompt == "y":
    age_two = int(input("What is the age of the second rider? "))
    height_two = int(input("What is the height of the second rider? "))

    if age_two in range (12,18):
        golden_passport2 = input("Do you have a golden passport?(Y/N) ").lower()

    # Case for riders less than 36 inches
    if height_one < 36 or height_two < 36:
        can_ride = False

    # Case for riders greater than or equals to 36 inches
    else:

        # Case for riders age 18 and above
        if age_one >= 18 or age_two >= 18 or golden_passport1 == "y" or golden_passport2 == "y": 
            # Golden passport and adults
            can_ride = True
        else:

            # Case for riders less than 18 years
            if age_one >= 12 and age_two >= 12 and height_one >= 52 and height_two >= 52:
                can_ride = True
            elif (age_one >= 16 or age_two >= 14) or (age_one >= 14 or age_two >= 16):
                can_ride = True
            else:
                can_ride = False

# Case for a single rider 
else:

    # 36 inches limit taken care of
    if (age_one >= 18 or golden_passport1 == "y") and height_one >= 62:
        can_ride = True
    else:
        can_ride = False


if can_ride:
    print("\nWelcome to the ride!")
else:
    print("\nSorry, this ride cannot go")