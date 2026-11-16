import pandas

data = pandas.read_csv("lifestyle_data.csv")

# What data type is `data` as output from the `read_csv()` method?
# Pandas DataFrame
#print(type(data))

# For each of the following pieces of information, try and use pandas to find the answer from the dataset in 'data'
# - You can open the csv file to see what data is available.
# - Use the pandas documentation to explore functions that you can use.
# - Leave your code under the comments.

# Find the total number of students
print(f"Total number of students: {data["GPA"].count()}")

# Find the mean average GPA of the students
print(f"Mean GPA of students: {data["GPA"].mean()}")

# Find the standard deviation of how much sleep students get per day
print(f"Standard deviation of sleep: {data["Sleep_Hours_Per_Day"].std()}")

# Find the maximum amount of study hours per day
print(f"Maximum number of study hours/day: {data["Study_Hours_Per_Day"].max()}")

# Sort the students by social hours per day ascending (lowest -> highest)
data.sort_values(by=["Social_Hours_Per_Day"])
print(data)

# Add a column 'Total_hours' which adds together all the Hours_Per_Day columns into one

# Filter all students with a 'high' stress level, and all the students with a 'low' stress level.
# Can you work out whether having a higher stress level leads to a higher GPA?
