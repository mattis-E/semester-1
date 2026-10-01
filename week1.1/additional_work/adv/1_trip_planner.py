"""Advanced Task 1: Trip Planner
- Ask for a destination name, total distance in miles, and planned travel time in hours.
- Convert the numeric inputs so you can calculate an approximate average speed for the journey.
- Display a human-readable summary that includes the destination and the speed formatted to two decimal places.
- Extension: warn if either numeric value is zero or negative.
"""

destination = input("Where are you going to? ")

distance_miles_input = input("How many miles will you travel? ")
time_hours_input = input("How many hours will the journey take? ")

if float(distance_miles_input) <= 0 or float(time_hours_input) <= 0:
    print("Distance or flight-time can't be less than or equal to zero!")
    quit()

# TODO: convert distance_miles_input and time_hours_input to numbers
distance_miles_input = float(distance_miles_input)
time_hours_input = float(time_hours_input)
# TODO: calculate the average speed in miles per hour
average_speed = (distance_miles_input / time_hours_input)
# TODO: print a summary message using an f-string
print(f"Your average speed will be {average_speed} mph")

# Extension: add validation for zero or negative values

"""
- histories & genealogies of languages
- learn rust
"""