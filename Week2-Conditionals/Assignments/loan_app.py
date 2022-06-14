# A program to determine if a user can qualify for a loan

print("\nWelcome to LoanBeta!")

# Get user input by asking a series of questions
print("\nPlease answer the following question by providing a rating from 1-10")
loan_size = int(input("\nHow large is the loan? "))
credit_history = int(input("How good is your credit history? "))
income = int(input("How high is your income? "))
down_payment = int(input("How large is your down payment? "))
print()

# Create boolean variable
# Adviseable to set to false in case of a situation where there is no else statement
should_loan = False

# Determine through user input if they are eligible for the loan or not
if loan_size >= 5:
    if credit_history >=7 and income >=7:
        should_loan = True
    elif credit_history >= 7 or income >= 7:
        if down_payment >= 5:
            should_loan = True
        else:
            should_loan = False
    else:
        should_loan = False
else:
    if credit_history < 4:
        should_loan = False
    else:
        if income >=7 or down_payment >= 7:
            should_loan = True
        elif income >= 4 and down_payment >= 4:
            should_loan = True
        else:
            should_loan = False

if should_loan:
    print("Congratulations! You are eligible to get a loan")
else:
    print("Sorry you are not eligible to get a loan")