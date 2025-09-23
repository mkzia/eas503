###############################################################
# for_ex1.py
# Write a function that takes in a list of values and returns its sum


def sum_list(input_list):
    summed_values = 0
    for value in input_list:
        summed_values += value

    return summed_values


print(sum_list([1, 2, 3, 4]))


###############################################################
# for_ex2.py
# Write a function that takes in a list of values and returns its average

def avg_list(input_list):
    summed_values = 0
    number_of_values = 0
    for value in input_list:
        summed_values += value
        number_of_values += 1

    return summed_values / number_of_values


print(avg_list([1, 2, 3, 4]))


##################################################################
# for_ex3.py
# Instead of using a for loop as in ex2, use sum() and len() to calculate the average

def avg_list(input_list):

    return sum(input_list) / len(input_list)


print(avg_list([1, 2, 3, 4]))


##################################################################
# for_ex4.py
# Write a function that multiplies the elements of the list and returns them

def multiply(input_list):
    output = []

    for ele in input_list:
        output.append(ele * 2)

    return output


print(multiply([1, 2, 3, 4]))


##################################################################
# for_ex5.py
# Write a pow() function that computes the power of each element in a list

def pow(input_list, power):
    output = []

    for ele in input_list:
        output.append(ele ** power)

    return output


print(pow([1, 2, 3, 4], 2))
print(pow([1, 2, 3, 4], 3))


##################################################################
# for_ex6.py
# Write a function to remove duplicate from a list


def remove_duplicate(input_list):
    return list(set(input_list))


print(remove_duplicate([1, 2, 3, 4, 4, 5, 1]))


##################################################################
# for_ex7.py
# Write a function that reads grades from an input file and calculates their average
# input: filename
# use: ex7_data1.txt
# use: ex7_data2.txt
# use: ex7_data3.txt
# use a list to read the values in to and then use sum and len to calclate average.
# Be careful about empty rows!
# Be careful about non-numbers!

def average_from_file(filename):
    grade_list = []
    with open(filename) as file:
        for line in file:
            if line.strip():
                try:
                    grade_list.append(float(line))
                except ValueError:
                    print('Bad value: ', line)

    return sum(grade_list) / len(grade_list)


print(average_from_file('for_ex7_data1.txt'))


##################################################################
# for_ex8.py
# Write a function simulates a coin toss
# Input: number of simulation
# Output: a string that concatenates the results, ex. 'HHHTTTHTHTHT'


def coin_toss(number):
    import random
    output = ''
    for i in range(number):
        toss = random.randint(0, 1)

        if number == 0:
            output += 'H'
        else:
            output += 'T'

    return output


print(coin_toss(10))


##################################################################
# for_ex9.py
# Write a function that uses the output from the coin_toss function and calculates the probablity of H and T
# Input: number of simulation
# Output: probabily of H and T

def coin_toss_probablity(number):
    result = coin_toss(number)
    head_count = 0
    tail_count = 0

    for ele in result:
        if ele == 'H':
            head_count += 1
        elif ele == 'T':
            tail_count += 1

    return (head_count / len(result), tail_count / len(result))


print(coin_toss_probablity(10))


##################################################################
# for_ex10.py
# Write a function that simultes coin_toss_probablity for a given number of times and calculates the average of H and T
# Input: number of simuations
# Input: number of coin tosses
# Output: average probability


def simulate_coin_toss_probablity(num_sims, num_toss):

    head_prob = 0
    tail_prob = 0

    for i in range(num_sims):
        h_prob, t_prob = coin_toss_probablity(num_toss)
        head_prob += h_prob
        tail_prob += t_prob

    return (head_prob / num_sims, tail_prob / num_sims)


print(simulate_coin_toss_probablity(10, 5))


##################################################################
# for_ex11.py
# Write a function that reads a file in which each line has multiple student grades and calculates the student average grade
# Print average of each student on screen
# Use list comprehension to convert grades to int
# use: for_ex11_data.txt

def print_student_average(filename):

    with open(filename) as file:
        for line in file:
            student_name, *tests = line.split(',')
            tests = [int(ele) for ele in tests]
            print(student_name, sum(tests)/len(tests))


print_student_average('for_ex11_data.txt')



##################################################################
# for_ex12.py
# Write a function that generates a given number of students with a given number of grades and saves them to a file
# inputs: output_filename, number_of_students, number_of_tests, test_score_range(low, high)
# example output:
# student1,93,78,82,83,65
# student2,86,76,85,86,65
# student3,70,98,88,80,93
# student4,89,68,81,80,76
# student5,99,67,100,83,68
# student6,75,77,69,72,76
# student7,67,93,90,92,66
# student8,89,83,90,97,91
# student9,92,84,75,92,92
# student10,65,89,80,68,89


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