# Week 4, Session 2: Task 1

# Write a function format_date that takes 4 arguments: day, month,
# year, separator. The separator is an optional argument with a default
# value to be "-". The function returns the formatted date as a string
# in the format day-month-year with the default separator.


def format_data(day, month, year, separator='-'):
    # complete your code here
    day =   str(day)
    month = str(month)
    year =  str(year)
    formatted_date = day + separator + month + separator + year
    return formatted_date


# Write code to test the function with separators such as "/", ":", "."
print(format_data(1, 1, 1990))
print(format_data(1, 1, 1990, ":"))
print(format_data(1, 1, 1990, "/"))
