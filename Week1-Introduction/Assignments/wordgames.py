# Mad Libs program


print("Welcome to Mad Libs!\n")
print("Please provide a word suggestion for the following prompts\n")


# Get user suggestions
adjective_word = input("Please input an example of an adjective: ")
animal_word = input("Please input an example of an animal: ")
verb_word1 = input("Please input an example of a verb: ")
exclamation_word = input("Please input an example of an exclamation: ")
verb_word2 = input("Please input an example of another verb: ")
verb_word3 = input("Please input an example of another verb: ")
silly_name1 = input("Please input an example of a silly name: ")
silly_name2 = input("Please input an example of another silly name: ")
verb_word4 = input("Please input an example of a verb in its past tense: ")
place_name = input("Please input an example of a place: ")
print()
# Print text
print("Here is your story:")
print()
print(f"The other day, I was really in trouble. It all started when \
I saw a very {adjective_word} {animal_word}\n{verb_word1} down the \
hallway. '{exclamation_word.capitalize()}!' I yelled. But all I \
could think to do was to\n{verb_word2} over and over. \
Miraculously, that caused it to stop, but not before it tried \
to\n{verb_word3} right in front of my family. I \
pulled {silly_name1} and {silly_name2} from harm's \
way and {verb_word4} to\nthe {place_name}")
print()
print("Thank you for playing the Mad Libs word game!")
