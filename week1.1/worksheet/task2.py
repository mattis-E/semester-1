"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Mattis Evans
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator, {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
monthly_savings = 0 # set it to an integer
monthly_savings = input("Enter your monthly savings amount: £")
# Validate that they have entered an integer.
try: # perhaps a bit janky, but isinstance didn't work, and this shows up early in thinkCSpy
    monthly_savings = int(monthly_savings)
except:
    print("Invalid amount")
    quit()

# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.
base_final_amount = monthly_savings * 12
print(f"You will save £{base_final_amount} every year")

# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).
interest_final_amount = base_final_amount * 1.008
print(f"With interest, you will save £{interest_final_amount:.2f} per year")
