"""Advanced Task 2: Budget Breakdown
- Ask for three separate expense amounts (for example: travel, food, accommodation).
- Convert each input so you can add them together to get a total trip cost.
- Calculate the average spend per category and show each value with an f-string.
- Extension: format the totals so they always show two decimal places.
"""

travel_cost_input = input("Travel cost in pounds: ")
food_cost_input = input("Food cost in pounds: ")
accommodation_cost_input = input("Accommodation cost in pounds: ")

# TODO: convert each value to a number type that supports decimals
travel_cost_input = float(travel_cost_input)
food_cost_input = float(food_cost_input)
accommodation_cost_input = float(accommodation_cost_input)

# TODO: calculate the total and the average spend per category
total_cost = travel_cost_input + food_cost_input + accommodation_cost_input
average_cost = total_cost / 3

# TODO: print the three costs, the total, and the average
print(f"Travel cost: £{travel_cost_input:.2f}")
print(f"Food cost: £{food_cost_input:.2f}")
print(f"Accommodation cost: £{accommodation_cost_input:.2f}")

print(f"Average cost: £{average_cost:.2f}")

# Extension: format the totals to two decimal places
