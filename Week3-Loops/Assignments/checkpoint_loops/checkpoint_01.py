# A program to ask for a positive number using a while loop

is_asking = True
while is_asking:
    number = float(input("Please enter a positive number: "))
    if number < 0:
        print("Sorry that is a negative number. Please try again.")
    else:
        print(f"The number is: {number}")
        break


# A program to stimulate a child asking their parent for a piece of 
# candy using a while loop 

ask_for_candy = True
while ask_for_candy:
    question = input("May I have a piece of candy?(Yes/No) ").lower()
    if question == "no":
        continue
    elif question == "yes":
        print("Thank you.")
        break
    else:
        print("That is not a required response")
