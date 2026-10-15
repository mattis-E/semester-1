# Week 1.3, Session 2: Calculate Average Grade and Write to a File

# Open 'student_data.csv' to read each student's grades
# hint: skip the header row with data[1:]
with open("student_data.csv", "r") as file:
    all_rows = file.readlines()

all_rows.pop(0)
student_average = {} # student_id, name, average.

for row in all_rows:
    row = row.split(",")
    row[4] = row[4].rstrip()
    print(row)

    id = row[0]
    name = row[1]
    average = (int(row[4]) + int(row[3]) + int(row[2])) / 3
    student_average[id] = [name, average]

# Read each student's grades and calculate their average grade
# hint: CSV data comes as strings, convert grade columns to int() for maths
# hint: student_data.csv has columns: ID, Name, Mathematics, Science, History
# hint: average = (maths + science + history) / 3


# Open a file called 'report.txt'
with open("report.txt", "w") as ofile:
    for test in student_average:
        print(test)
# Write each student's name and their average grade to the report
# hint: use 'w' mode to create a fresh report each time
# hint: format averages nicely, maybe to 2 decimal places with :.2f
