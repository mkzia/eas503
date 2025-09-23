# import sys

# try:
#     n = int(input("How many numbers do you have? "))
#     if n < 1:
#         print('Please enter a value an integer than 0 !')
#         sys.exit()
# except ValueError as error:
#     print(error)
#     print('Please enter a number!')
#     sys.exit()



# sum = 0.0
# for i in range(n):
#     x = float(input("Enter a number >> "))
#     sum = sum + x
# print("\nThe average of the numbers is", sum / n)


# i = 0
# while i <= 10:
#     print(i)
#     # i = i + 1


# sum = 0.0
# count = 0
# moredata = "yes"
# while moredata.lower() == "yes":
#     x = float(input("Enter a number >> "))
#     sum = sum + x
#     count = count + 1
#     moredata = input("Do you have more numbers (yes or no)? ")
# print("\nThe average of the numbers is", sum / count)


# sum = 0.0
# count = 0
# x = float(input("Enter a number (negative to quit) >> "))
# while x >= 0:
#     sum = sum + x
#     count = count + 1
#     x = float(input("Enter a number (negative to quit) >> "))
# print("\nThe average of the numbers is", sum / count)


# sum = 0.0
# count = 0
# xStr = input("Enter a number (<Enter> to quit) >> ")
# while xStr != "":
#     x = float(xStr)
#     sum = sum + x
#     count = count + 1
#     xStr = input("Enter a number (<Enter> to quit) >> ")
# print("\nThe average of the numbers is", sum / count)


# fileName = input("What file are the numbers in? ")
# infile = open(fileName,'r')
# sum = 0.0
# count = 0
# for line in infile:
#     if not line.strip():
#         continue
#     if line.strip() == 'NaN' or line.strip() == '.':
#         print(f'Encountered a non number: {line.strip()}')
#         continue
#     print(line.strip())
#     sum = sum + float(line)
#     count = count + 1
# print("\nThe average of the numbers is", sum / count)

import math
fileName = input("What file are the numbers in? ")
infile = open(fileName,'r')
sum = 0.0
count = 0
line = infile.readline()
while line:
    print(line.strip())
    try:
        number = float(line)
        if math.isnan(number):
           line = infile.readline()
           continue
        sum = sum + float(line)
    except Exception as error:
        print(error)
        line = infile.readline()
        continue
    count = count + 1
    line = infile.readline()
print("\nThe average of the numbers is", sum / count)


# fileName = input("What file are the numbers in? ")
# infile = open(fileName,'r')
# sum = 0.0
# count = 0
# line = infile.readline()
# while line != "":
#     # update sum and count for values in line
#     for xStr in line.split(","):
#         sum = sum + float(xStr)
#         count = count + 1
#     line = infile.readline()
# print("\nThe average of the numbers is", sum / count)

## Add try

# while True:
#     number = float(input("Enter a positive number: "))
#     if number >= 0:
#         break # Exit loop if number is valid


# e
# ans = input("What flavor do you want [vanilla]: ") or "vanilla"
# print(ans)

# https://realpython.com/python-conditional-statements/
# x = y = 40
# z = 1 + x if x > y else y + 2

# z = 1 + (x if x > y else y) + 2
