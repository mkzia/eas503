##############################################################
# dict_ex1.py
# Load people.tsv into a dictionary. 
# Prompt user for filename

from pprint import pprint
filename = 'people.tsv'

with open(filename) as file:
	header = None
	students = []
	for line in file:
		line = line.strip()
		if header is None:
			header = line.split('\t')
			continue

		student = line.split('\t')
		tmp_dict = dict(zip(header,student))
		students.append(tmp_dict)




print(students[67]['country'])


