# Worksheet 1.3: Task 3

# Your code for the overall grade classification

# ask for filename of the student file
#fn = input("Filename: ")
fn = "student_data_10.csv"

# open the file
f = open(fn)

# read in the data, and for each student calculate their average grade and classification
lines = []
for l in f:
    lines.append(l)
f.close()
del f

lines.pop(0) # remove header line

student_data_aggregate = [] # student_1, ..., student_n
student_data = []           # ID, module_1, ... module_n
student_counter = 0
# for each line:
for l in lines:
    start = 0   
    counter = 0
    for c in l: # get individual values from a single student
        if c == "," and start == 0:
            student_data.append(l[start:counter])       # student ID
            start = counter
        elif len(l) - counter <= 2 and c != ",":        # last score, if applicable. number of digits if no comma at the end (c.f. below)
            student_data.append(l[start + 1:len(l) - 1])
            break
        elif len(l) - counter <= 3 and c != ",":        # last score, if applicable.
            student_data.append(l[start + 1:len(l) - 2])
            break
        elif c == "," and start != 0:
            student_data.append(l[start + 1:counter])   # all scores under the last one
            start = counter
        counter += 1
    # now remove the commas
    student_data[:] = (n for n in student_data if n != ',' and n != '')
    # and add it to student_data_aggregate
    student_data_aggregate.append(student_data)
    student_data = []

# calculate average
all_students = []
student_stat = []
student_counter = 0
sum = 0
for i in student_data_aggregate:    # for all students
    for j in i:                     # for each student  
        j = str(j)
        if j.isnumeric():           # if it's a module score
            j = int(j)
            sum += j                # add it to the sum
    student_stat.append(student_data_aggregate[student_counter][0])
    mean = sum / (len(student_data_aggregate[student_counter]) - 1)
    mean = round(mean, 2)
    student_stat.append(mean)
    all_students.append(student_stat)
    student_stat = []
    student_counter += 1
    mean = 0
    sum = 0

# write out this calculated data in the format without a header:
#      student_id,average_grade,classification - replace this with actual value
#      The average grade should be given to 2 decimal places
#      this can be achieved by using the following in an fstring: {variable_name:.2f}

# Write to output.
fn += "_out.csv"
f = open(fn, "a")
for d in all_students:
    sc = ""
    if d[1] >= 70:
        sc = "1"
    elif 60 <= d[1] <= 70:
        sc = "2:1"
    elif 50 <= d[1] <= 60:
        sc = "2:2"
    elif 40 <= d[1] <= 50:
        sc = "3"
    else:
        sc = "F"

    f.write(f"{d[0]},{d[1]:.2f},{sc}\n")
f.close()

# write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'

# You can compare your output files with the 4 example files in example_outfiles folder