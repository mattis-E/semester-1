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
        elif c == "," and start != 0:
            student_data.append(l[start + 1:counter])   # all scores under the last one
            start = counter
        elif len(l) - counter <= 3 and c != ",":        # last score, if applicable.
            student_data.append(l[start + 1:len(l) - 1])
            break
        counter += 1
    # now remove the commas
    student_data[:] = (n for n in student_data if n != ',' and n != '')
    # and add it to student_data_aggregate
    student_data_aggregate.append(student_data)
    student_data = []

print(student_data_aggregate)

# write out this calculated data in the format without a header:
#      student_id,average_grade,classification - replace this with actual value
#      The average grade should be given to 2 decimal places
#      this can be achieved by using the following in an fstring: {variable_name:.2f}


# write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'

# You can compare your output files with the 4 example files in example_outfiles folder