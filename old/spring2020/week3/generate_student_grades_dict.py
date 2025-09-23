import json
import random

number_of_students = 100
number_of_tests = 5
test_score_range = (65, 100)

grades = []
for i in range(1, number_of_students+1):
    tmp = {}
    student_name = 'student' + str(i)
    tmp['name'] = student_name
    for ii in range(number_of_tests):
        key = 'test' + str(ii+1)
        score = random.randint(test_score_range[0], test_score_range[1])
        tmp[key] = str(score)

    grades.append(tmp)

with open('grades_dict.json', 'w') as outfile:
    json.dump(grades, outfile, sort_keys=True, indent=4, ensure_ascii=False)

with open('grades_dict.json') as infile:
    grades = json.load(infile)