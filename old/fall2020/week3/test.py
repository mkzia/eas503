def generate_students(output_filename, number_of_students, number_of_tests, test_score_range):

    import csv
    import random

    # number_of_students = 10
    # number_of_tests = 5
    # test_score_range = (65, 100)

    csvfile = csv.writer(open(output_filename, 'w'), delimiter=',')

    for i in range(1, number_of_students+1):
        line = []
        student_name = 'student' + str(i)
        line.append(student_name)
        for ii in range(number_of_tests):
            line.append(random.randint(test_score_range[0], test_score_range[1]))

        csvfile.writerow(line)


generate_students('testdata.txt', 10, 3, (65,100))