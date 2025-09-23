import csv
import random

number_of_students = 100
number_of_tests = 5
test_score_range = (65, 100)

csvfile = csv.writer(open('ex3_data.txt', 'w'), delimiter=',')

for i in range(1, number_of_students+1):
    line = []
    student_name = 'student' + str(i)
    line.append(student_name)
    for ii in range(number_of_tests):
        line.append(random.randint(test_score_range[0], test_score_range[1]))

    csvfile.writerow(line)

