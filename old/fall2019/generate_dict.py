from faker import Faker
import random
fake = Faker()
import csv

lines = []

for i in range(100):
    last_name = fake.last_name()
    first_name = fake.first_name()
    email = fake.email()
    country = fake.country()
    account = fake.bban() 

    lines.append((last_name, first_name, email, country, account))

datafile = open('people.tsv', 'w')
writer = csv.writer(datafile, delimiter='\t')
header = ['last_name', 'first_name', 'email', 'country', 'account']
writer.writerow(header)
for line in lines:
    writer.writerow(line)
