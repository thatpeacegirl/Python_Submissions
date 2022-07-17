# A shopping cart program where users can add items to the cart, 
# remove items, view the contents of the cart, and see
# the total price of items in the cart.


# Import modules
from datetime import datetime
import time

# Declare variables
items = []
prices = []
total = 0
cart_option = True

# Display a message
print("Welcome to the Shopping Cart Program!")
time.sleep(1)
user_name = input("What is your name? ").upper()

# Loop the program as long as the boolean variable is true
while cart_option:
    time.sleep(2.5)
    print()
    # Display a message
    print("Please select one of the following:")
    print("1. Add an item")
    print("2. View cart")
    print("3. Remove an item")
    print("4. Compute the total")
    print("5. Show your receipt")
    print("6. Quit")
    print()
    time.sleep(2)
    
    # Get user input
    menu_option = int(input("Select an option: "))
    time.sleep(1)

    # Condition if user choice is 1
    if menu_option == 1:
        # Get user input
        new_item = input("What item would you like to add? ").capitalize()

        # Add each user input to the end of the list
        items.append(new_item)
        time.sleep(1)

        # Get user input
        print(f"What is the price of '{new_item}'? ", end="")
        new_item_price = int(input())

        # Add each user input to the end of the list
        prices.append(new_item_price)
        time.sleep(1)
        print(f"'{new_item}' has been added to the cart")
        
    # Condition if user choice is 2
    elif menu_option == 2:
        # Print out the desired output using the index of items in a list
        print("\nThe contents of the shopping cart are:")
        time.sleep(1)
        for i in range(len(items)):
            item = items[i]
            price = prices[i]
            print(f"{i+1}. {item} - ${price}")
    
    # Condition if user choice is 3
    elif menu_option == 3:
        # Get user input
        remove_item = int(input("Which item would you like to remove? "))
        remove_item -= 1
        time.sleep(1)

        # Condition if user tries to remove an item with an invalid index
        if remove_item >= len(items):
            print("Sorry that is not a valid item number")
        else:
            # Remove item with the specified index
            items.pop(remove_item)
            prices.pop(remove_item)
            print("Item removed")
    
    # Condition if user choice is 4
    elif menu_option == 4:
        # Add all the items in the prices list together
        for j in range(len(prices)):
            price = prices[j]
            total += price
        print(f"The total price of the items in the shopping cart is ${total:.2f}")
    
    # Condition if user choice is 5
    elif menu_option == 5:

        # Condition if user has not computed the total price of items
        if total == 0:
            print("You have to compute the total to be able to show the receipt")

        else:
            # Use datetime library to display date and time in a format
            current_date = datetime.now()
            print()
            print(f"Customer name: {user_name}")
            print(f"Date: {current_date.date()}")
            print(f"Time of purchase: {current_date.strftime('%X')}")
            print()
            print("Items     Price")

            # Display the receipt
            for k in range(len(items)):
                item = items[k]
                price = prices[k]
                print(f"{item:10}${price}")
            print()
            print(f"TOTAL:    ${total:.2f}")
 
    # Condition if user choice is 6
    else:
        # End the program
        print("Thank you for using our program")
        break










"""
Pseudocode:

BEGIN

FROM datetime  IMPORT datetime

Declare variables
items = []
prices = []
total = 0
cart_option = True

PRINT: "Welcome to the Shopping Cart Program!"
user_name = INPUT: "What is your name? "

WHILE cart_option:

    PRINT: "Please select one of the following:
    1. Add a new item
    2. Display the contents of the shopping cart
    3. Remove an item
    4. Compute the total
    5. Show your receipt
    6. Quit"

    menu_option = INT(INPUT: "Select an option: ")

    IF menu_option = 1:

        new_item = INPUT: "What item would you like to add? "
        APPEND(items, new_item)
        new_item_price = INT( INPUT: "What is the price of (new_item)?")
        APPEND(prices, new_item_price)
        PRINT: "(new_item) has been added to the cart"

    ENDIF

    ELIF menu_option = 2:

        PRINT: "The contents of the shopping cart are:"

        FOR i = range(nummber of new_item in items):
            item = items[i]
            price = prices[i]

            PRINT: "(i + 1). (item) - $(price)"
        ENDFOR

    ENDELIF

    ELIF menu_option = 3:

        remove_item = INT( INPUT: "Which item would you like to remove? ")
        remove_item -= 1

        IF remove_item >= (nummber of new_item in items):
            PRINT: "Sorry that is not a valid item number"
        ENDIF

        ELSE:
            REMOVE(items, remove_item)
            REMOVE(prices, remove_item)
            PRINT: "Item removed
        ENDELSE

    ENDELIF

    ELIF menu_option = 4:

        FOR j = range(nummber of new_item in items):
            price = prices[j]
            total += price
        ENDFOR
    PRINT: "The total price of the items in the shopping cart is $(total)"

    ENDELIF

    ELIF menu_option = 5:
        IF total == 0:
            PRINT: "You have to compute the total to be able to show the receipt"
        ENDIF
    
        ELSE
            current_date = datetime.now()
            PRINT: "Customer name: (user_name)"
            PRINT: "Date: (current_date.date())"
            PRINT: "Time of purchase: (current_date.strftime('%X'))"
            PRINT: "Items     Price"

            FOR k = range(nummber of new_item in items):
                item = items[k]
                price = prices[k]
                PRINT: "(item:10)$(price)"
            ENDFOR
            
            PRINT: "TOTAL:    $(total)"
        ENDELSE

    ENDELIF
 
    ELSE:
        break
    ENDELSE

ENDWHILE

END
"""

# Display correct total on the list if user has already 
# computed the total but removes an item or adds a new item?