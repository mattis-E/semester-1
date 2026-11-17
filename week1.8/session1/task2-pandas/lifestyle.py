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
print(data.sort_values(by=["Social_Hours_Per_Day"], ascending=True))

# Add a column 'Total_hours' which adds together all the Hours_Per_Day columns into one
for index, row in data.iterrows():
    total_hours = row["Sleep_Hours_Per_Day"] + row["Study_Hours_Per_Day"] + row["Physical_Activity_Hours_Per_Day"] + row["Social_Hours_Per_Day"] + row["Extracurricular_Hours_Per_Day"]
data.insert(6, "Total_hours", total_hours)
print(data)

# Filter all students with a 'high' stress level, and all the students with a 'low' stress level.
# Can you work out whether having a higher stress level leads to a higher GPA?
# average GPA of students with a high stress level:
high_gpas = []
hgpa_sum = 0
low_gpas = []
lgpa_sum = 0
for index, i in data.iterrows():
    if i["Stress_Level"] == "High":
        high_gpas.append(i["GPA"])
    elif i["Stress_Level"] == "Low":
        low_gpas.append(i["GPA"])
for i in high_gpas:
    hgpa_sum += i 
for i in low_gpas:
    lgpa_sum += i
print("###############")
print(f"Average GPA of students with a high stress level: {hgpa_sum / len(high_gpas)}")
# average GPA of students with a low stress level:
print(f"Average GPA of students with a low stress level: {lgpa_sum / len(low_gpas)}")