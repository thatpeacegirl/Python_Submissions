def main():
        # Create and print a list named fruit.
        fruit_list = ["pear", "banana", "apple", "mango"]
        print(f"original: {fruit_list}")

        # Reverse and print fruit_list
        fruit_list.reverse()
        print(f"reversed: {fruit_list}")

        # Append "orange" to the end of fruit_list and print the list
        fruit_list.append("orange")
        print(f"append orange: {fruit_list}")

        # Find location of "apple", insert "cherry" before
        # "apple" in the list and print the list
        fruit_list.insert(fruit_list.index("apple"), "cherry")
        print(f"insert cherry: {fruit_list}")

        # Remove "banana" from fruit_list and print
        fruit_list.remove("banana")
        print(f"remove banana: {fruit_list}")

        # Pop the last element from fruit_list and
        # print the popped element and the list
        last_element = fruit_list[-1]
        fruit_list.pop()
        print(f"pop {last_element}: {fruit_list}")

        # Sort and print fruit_list
        fruit_list.sort()
        print(f"sorted: {fruit_list}")

        # Delete "mango" from the fruit_list, and
        # insert "cashew" in its place, then print the list
        fruit_list.insert(fruit_list.index("mango"), "cashew")
        fruit_list.pop(fruit_list.index("mango"))
        print(f"delete and insert: {fruit_list}")

        # Find and print the length of the fruit_list
        fruit_list_length = len(fruit_list)
        print(f"length: {fruit_list_length}")

        # Clear and print fruit_list

        fruit_list.clear()
        print(f"cleared: {fruit_list}")
    # Call main to start this program
if __name__ == "__main__":
    main()