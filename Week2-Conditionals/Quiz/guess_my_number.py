# A number guessing game to guess a stored number

# Store number to guess
answer = 306

# Take user Input
guess= int(input("\nEnter your guess: "))

# Do comparisons to check if input is the same as saved variable

# Guess value less than stored variable
if guess < answer:
    result = "Oops! Your guess was too low."

# Guess value is greater than stored variable
elif guess > answer:
    result = "Oops! Your guess was too high."

# Guess value is the same as stored variable
elif guess == answer:
    result = "Nice! Your guess matched the answer!"

print(result)