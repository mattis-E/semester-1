# To test that you can successfully download a file and upload it to gradescope

# You are going to write a very simple program:

# Validation
try:
    # Ask a user to enter two numbers (one per input)
    num1 = input("Enter the first integer: ")
    num2 = input("Enter the second integer: ")

    num1 = int(num1)
    num2 = int(num2)
except:
    print("You didn't enter two integers!")
    quit()

# multiply those numbers together
Product = num1 * num2

# print out the result
print(f"{Product = }")

# There is an extra point available for validating that they entered numbers!
# Add to your code so that if they entered something other than an integer it prints
# 'That is not a number' and exits.

# Download your file, and upload it to the 'Week 1 Session 2 - Practice Upload' task on Minerva.
# You will get some feedback - ensure you are passing the tests!