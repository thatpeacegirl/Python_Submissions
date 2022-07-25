# A program to open a file, read through it line by line, strip off leading and trailing whitespace and display each book to the screen.

# Open up the books.txt file
with open("books.txt") as book_of_mormon:
    # Iterate through each line in the file
    for line in book_of_mormon:
        # Strip each line of any leading or trailing whitespace
        line = line.strip()
        # Print the clean line
        print(line)
        
# Close the books.txt file