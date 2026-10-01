"""Advanced Task 4: Deadline Breakdown
- Ask how many minutes remain until an assignment deadline.
- Use integer division and modulo to convert this number into days, hours, and minutes.
- Present the result using a formatted string such as "2 days, 3 hours, 15 minutes remaining".
- Extension: handle negative input by printing a warning that the deadline has already passed.
"""

minutes_remaining_input = input("Minutes remaining until the deadline: ")

# TODO: convert the input to an integer
minutes_remaining_input = int(minutes_remaining_input)

# TODO: calculate whole days, leftover hours, and remaining minutes
# 1440 minutes in a day
days_left = minutes_remaining_input // 1440
hours_left = (minutes_remaining_input % 1440) // 60
minutes_left = (minutes_remaining_input % 1440) % 60

# TODO: print the breakdown using f-strings
print(f"Time left: {days_left} days, {hours_left} hours, and {minutes_left} minutes.")
# Extension: detect negative values and print a warning instead
