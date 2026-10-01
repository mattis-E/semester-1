"""Advanced Task 5: Safe Divider
- Ask for a numerator and a denominator.
- Convert both inputs to integers and divide them to get a result.
- Use try/except to catch both non-numeric input and division by zero, giving useful messages for each case.
- Only print the final answer when the calculation succeeds.
"""

numerator_input = input("Enter the numerator: ")
denominator_input = input("Enter the denominator: ")
result = 0

try:
    numerator_input = int(numerator_input)
    denominator_input = int(denominator_input)
    result = numerator_input / denominator_input
except:
    print("A non-integer was entered, or division by zero occurred!")
    quit()

print(f"Result: {result}")

# TODO: wrap the risky operations in a try/except block
# TODO: convert the values to integers and perform the division
# TODO: print clear feedback when something goes wrong
# TODO: only show the answer when the division succeeds
