from faker import Faker
import random
fake = Faker()
import csv

lines = []

for i in range(100):
    name = f'{fake.last_name()}, {fake.first_name()}'
    credit_hours = random.randint(1,140)
    while True:
        tmp = random.randint(1,400)
        if tmp/credit_hours < 4.0 and tmp/credit_hours > 1.5:
            q_point = tmp
            break
    lines.append((name, credit_hours, q_point))

datafile = open('data.tsv', 'w')
writer = csv.writer(datafile, delimiter='\t')
for line in lines:
    writer.writerow(line)
