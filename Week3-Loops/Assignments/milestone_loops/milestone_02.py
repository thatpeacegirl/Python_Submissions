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
