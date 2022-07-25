# A program to display a paycheck for employees
# who have their data in a text file

# Open up the hr_system.txt file
with open("hr_system.txt") as employee_info:
    # Iterate through each line in the file
    for line in employee_info:
        # Strip each line of any leading or trailing whitespace
        line = line.strip()
        # Split the item using a whitespace
        employee_data = line.split(" ")
        # Assign the split items to a variable using their indexes
        name = employee_data[0]
        id_number = employee_data[1]
        job_title = employee_data[2]
        salary = float(employee_data[3])

        # Perform calculations
        monthly_salary = salary / 24

        # Conditional if the employee is an Engineer
        if job_title == "Engineer":
            bonus = 1000
            monthly_salary += bonus

        # Print a statement to the screen 
        print(f"{name} (ID: {id_number}), {job_title} - ${monthly_salary:.2f}")

# Close the hr_system.txt file