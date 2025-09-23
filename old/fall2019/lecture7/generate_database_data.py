from faker import Faker
import random
fake = Faker()
import csv

lines = []

for i in range(100):
    last_name = fake.last_name()
    first_name = fake.first_name()
    username = last_name.lower() + first_name[:4].lower()
    exam1 = random.randint(1,101)
    exam2 = random.randint(1,101)
    exam3 = random.randint(1,101)
    

    lines.append((last_name, first_name, username, exam1, exam2, exam3))

datafile = open('students.tsv', 'w')
writer = csv.writer(datafile, delimiter='\t')

for line in lines:
    writer.writerow(line)
