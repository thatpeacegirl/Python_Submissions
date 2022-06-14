# A program to create an id badge for a Nigerian
# Get users details



print("Please enter the following information:")
first_name  = input("First name: ")
last_name = input("Last name: ")
email = input("Email address: ")
phone_no = input("Phone number: ")
job_title = input("Job title: ")
id_no = input("ID Number: ")
hair_color = input("Hair color: ")
eye_color = input("Eye color: ")
start_month = input("Start month: ")
training = input("Training(Yes/No): ")

# Removing first zero from phone number
phone_no = phone_no[1:]

# Display ID Badge
print("\nThe ID Card is:")
print("-" * 40)
print(f"{last_name.upper()}, {first_name.capitalize()}")
print(job_title.title())
print(f"ID: {id_no}")
print()
print(email.lower())
print(f"(+234){phone_no}")
print()
print(f"Hair: {hair_color.capitalize():15} Eyes: {eye_color.capitalize()}")
print(f"Month: {start_month.capitalize():14} Training: {training.capitalize()}")
print("-" * 40)


# Case of user inputing country code not taken into consideration
# Spacing between phone number digits and id number not defined
