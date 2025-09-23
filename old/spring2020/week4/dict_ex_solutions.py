##############################################################
# dict_ex1.py
# Load people.tsv into a dictionary. Prompt user for filename

## populating a dictionary from a file
filename = input('What is the name of the file? ')
header = None
data_array = []

with open(filename, 'r') as fp:
    for line in fp:
        if header is None:
            header = line.strip().split('\t')
            continue

        data_array.append(dict(zip(header, line.strip().split('\t'))))

from pprint import pprint
pprint(data_array)



####################################################
# dict_ex2.py 
# Write a function to convert month number to 
# month name. First use a list and then a dictionary

def convert_to_month_list(month):

months = [
	'',
	'January',
	'February',
	'March',
	'April',
	'May',
	'June',
	'July',
	'August',
	'September',
	'October',
	'November',
	'December',
]

	return months[month]

print(convert_to_month_list(3))

def convert_to_month_dict(month):

	months = {
		1: 'January',
		2: 'February',
		3: 'March',
		4: 'April',
		5: 'May',
		6: 'June',
		7: 'July',
		8: 'August',
		9: 'September',
		10: 'October',
		11: 'November',
		12: 'December',
	}


	return months[month]

print(convert_to_month_list(3))


####################################################
# dict_ex3.py 
# Convert text message to numbers

# 0 	space
# 1 	., ?, !
# 2 	ABC
# 3 	DEF
# 4 	GHI
# 5 	JKL
# 6 	MNO
# 7 	PQRS
# 8 	TUV
# 9 	WXYZ

def convert_message_to_numbers(message):

    lookup = {
        0: ' ',
        1: '.,?!',
        2: 'ABC',
        3: 'DEF',
        4: 'GHI',
        5: 'JKL',
        6: 'MNO',
        7: 'PQRS',
        8: 'TUV',
        9: 'WXYZ'
    }


    lookup_map = {}

    for key, value in lookup.items():
        for ele in value:
            lookup_map[ele] = key


    # order is important!!!!
    lookup_map = {ele: key for key, value in lookup.items() for ele in value }

    # order incorrect
    # lookup_map = {ele: key for ele in value  for key, value in lookup.items()}


    # lookup = (
    #     (0, ' '),
    #     (1, '.,?!'),
    #     (2, 'ABC'),
    #     (3, 'DEF'),
    #     (4, 'GHI'),
    #     (5, 'JKL'),
    #     (6, 'MNO'),
    #     (7, 'PQRS'),
    #     (8, 'TUV'),
    #     (9, 'WXYZ'),
    # )


    # lookup_map = {}

    # for key, value in lookup:
    #     for ele in value:
    #         lookup_map[ele] = key


    numbers = ''
    for char in message:
        numbers += str(lookup_map[char.upper()])



    lookup_map = {ele: str(key)*idx for key, value in lookup.items() for idx, ele in enumerate(value, 1)  }

    print(lookup_map)

    numbers = ''
    for char in message:
        numbers += lookup_map[char.upper()]


    return numbers


print(convert_message_to_numbers('Hello, World!'))


####################################################
# dict_ex4.py 
# Write a function that uses enumerate to print the index and value from range.
# Use vary the enumerate start index

def test_enumerate(range_value):

    for index, value in enumerate(range(range_value), 1):
        print(index, value)

test_enumerate(10)



######################################################
# dict_ex5.py
# Simulate two dice. Print the total, theoretical/expected probability, and simulated probability
# input: the number of simulations
# https://socratic.org/questions/what-is-the-expected-value-of-the-sum-of-two-rolls-of-a-six-sided-die
# Total     Simulated Percent     Expected Percent 

# 2                      2.76                 2.78
# 3                      5.57                 5.56
# 4                      8.34                 8.33
# 5                      11.1                11.11
# 6                     13.83                13.89
# 7                     16.68                16.67
# 8                      13.9                13.89
# 9                      11.1                11.11
# 10                     8.36                 8.33
# 11                     5.57                 5.56
# 12                     2.79                 2.78


def simulate_two_dice(no_simulation):
    import random
    theoretical_probabilities = [
        0,
        0,
        1 / 36,
        2 / 36,
        3 / 36,
        4 / 36,
        5 / 36,
        6 / 36,
        5 / 36,
        4 / 36,
        3 / 36,
        2 / 36,
        1 / 36,
    ]

    two_dice = {}

    for no in range(no_simulation):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        total = dice1 + dice2
        if total not in two_dice:
            two_dice[total] = 0

        two_dice[total] += 1

    simulated_probability = [0, 0]

    for number in range(2, 13):
        simulated_probability.append(two_dice[number] / no_simulation)

    column1 = 'Total'
    column2 = 'Simulated Percent'
    column3 = 'Expected Percent'

    print(
        column1.ljust(6),
        column2.rjust(20),
        column3.rjust(20),
        '\n'
    )
    for number in range(2, 13):
        sp = round(simulated_probability[number] * 100, 2)
        tp = round(theoretical_probabilities[number] * 100, 2)
        print(
            str(number).ljust(6),
            str(sp).rjust(20),
            str(tp).rjust(20),
        )


simulate_two_dice(1000000)