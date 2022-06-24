# Iterating Through Strings

"""
A program that asks the user for their favorite letter. Then, loops through all the words in the provided list, and for each word, loops through all of it's letters. If the letter is the user's favorite, print it out as a capital letter, if not, print it out as a lower case letter.
"""


word = "Commitment".lower()
fav_letter = input("What is your favorite letter? ").lower()
for letter in word:
    if letter == fav_letter:
        print(letter.replace(letter, "_"), end = "")
    else:
        print(letter, end = "")



# Stretch challenge program

program_run = "y"

while program_run == "y":
    word = "In coming days, it will not be possible to survive spiritually without \
the guiding, directing, comforting, and constant influence of the Holy Ghost."

    letter_number = int(input("Please enter a number: "))

    for index, letter in enumerate(word):
        if index % letter_number == 0:
            print(letter.upper(), end = "")
        else:
            print(letter.lower(), end = "")

    program_run = input("\nWould you like to enter another number?(Y/N) ")
    program_run = program_run.lower()
    
print("Goodbye")