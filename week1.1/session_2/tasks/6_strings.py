# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}")                          # prints original string
print(f"Modified String 1: {user_string.lower()}")                  # prints lowercase version of string
print(f"Modified String 2: {user_string.upper()}")                  # prints uppercase version of string
print(f"Modified String 3: {user_string.strip()}")                  # removes leading and ending whitespace from the string
print(f"Modified String 4: {user_string.replace('a', '@')}")        # replaces 'a' characters with '@'
print(f"Modified String 5: {user_string.capitalize()}")             # capitalises first letter of string 
print(f"Modified String 6: {user_string[::-1]}")                    # prints string in reverse
print(f"Modified String 7: {user_string.title()}")                  # prints the string with every letter after a non-letter character capitalised.
print(f"Modified String 8: {len(user_string)}")                     # prints length of string
print(f"Modified String 9: {user_string.find('a')}")                # prints first index of the character 'a' in the string
print(f"Modified String 10: {user_string.count('a')}")              # counts the occurences of the character 'a' in the string
print(f"Modified String 11: {user_string.startswith('Hello')}")     # prints True if the string starts with the word 'Hello'
print(f"Modified String 12: {user_string.endswith('!')}")           # prints True if the string ends with the character '!'
print(f"Modified String 13: {user_string.isalnum()}")               # prints True if the string is made up only of numbers and characters (if it's alphanumerical)
print(f"Modified String 14: {user_string.isalpha()}")               # prints True if the string is made up only of characters.
print(f"Modified String 15: {user_string.isdigit()}")               # prints true if the string is made up only of numbers



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!