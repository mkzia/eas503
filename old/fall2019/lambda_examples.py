# def square(num):
#     return num * num


# square2 = lambda num: num * num
# # lambda a function without a name;
# # anonymous functions;
# # one line only;
# # single expression only
# # stored in a variable
# # When do you use it? Pass a function into another function as a parameter
# # lambda variables (comma separated): expression

# print(square(9))

# print(square2(9))

# add = lambda a,b: a + b

# print(add(3,10))


# func = lambda a, b: a * b
# def lambda_test(function, number1, number2):
#     return function(number1, number2)


# print(lambda_test(func, 3, 4))

# # lambda functions are used with other functions. Usually with map, filter, sort

# my_list = [2, 3, 4]

# # double this list

# # method 1 - define a square function

# def square_list(my_list):
#     new_list = []
#     for ele in my_list:
#         new_list.append(ele * ele)

#     return new_list

# print(square_list(my_list))

# # method 2 - list comprehension

# print([ele*ele for ele in my_list])

# # method 3 - use lambda with map
# # map(lambda variables (comma separated): expression)

# print(list(map(lambda ele: ele*ele, my_list)))

# # # map objects are a generator. How many times can you iterate over them?

# students = ['john', 'jane', 'doe']

# # make upper case


# # method 1 create new list and loop
# new_list = []
# for student in students:
#     new_list.append(student.title())

# print(new_list)

# # method 2 -- use list comprehension

# print([student[0].upper()+student[1:] for student in students])

# # method 3 -- use lambda

# print(list(map(lambda student: student.title(), students)))


# # covert each value to float

# my_dict = [{'value': '34.4'}, {'value': '45.3'}, {'value': '73.4'}]

# print(list(map(lambda ele: {'Value': float(ele['value'])}, my_dict)))


# # # Filter -- basically, combining conditional and lambda. Will return all expressions
# # # that evaluate to True
# # # filter(lambda variables (comma seperated): expression (that will evaluate to True or False/None), list))


# years = range(1970, 2000)

# def is_leap_year(year):
#     # does not work for century year
#     if year % 4 == 0:
#         return True
#     else:
#         return False

# my_dict = {}
# leap_years = []
# for year in years:
#     my_dict.update({year: is_leap_year(year)})
#     if is_leap_year(year):
#         leap_years.append(year)

# import pprint
# pprint.pprint(my_dict)
# print(leap_years)


# def square(num):
#     return num * num


# print(list(map(square, range(5))))

# print(list(filter(lambda year: year % 4 == 0, range(1970, 2000))))
# print(list(filter(lambda year: is_leap_year(year), range(1970, 2000))))
# print(list(map(lambda year: year/5, filter(lambda year: year % 4 == 0, range(1970, 2000)))))

# # # combining map with filter

# print(list(map(lambda year: f'{year} is a leap year!', filter(lambda year: year % 4 == 0, range(1970, 2000)) )))


# # # list comprehension

# # print()
# print([f'{year} is a leap year' for year in range(1970, 2000) if year % 4 == 0])






# x = (('efg', 1), ('abc', 3), ('hij', 2))

# print(sorted(x)) # does work

# print(sorted(x, key=lambda ele: ele[1]))


students = [
    {'username': 'john', 'grade': 50},
    {'username': 'jane', 'grade': 80},
    {'username': 'doe', 'grade': 35},
    {'grade': 89, 'username': 'Kelly'}
]


# from pprint import pprint
# print(sorted(students, key=lambda student: student['username']))
# print()
# print(sorted(students, key=lambda student: student['username'], reverse=True))
# print()
# print(sorted(students, key=lambda student: student['grade']))
# print()
# print(sorted(students, key=lambda student: student['grade'], reverse=True))



students = ['john', 'Janette', 'doe']

print(min(students))


print(min(students, key=lambda student: len(student)))

print(max(students, key=lambda student: len(student)))


my_list = [{'value': '34.4'}, {'value': '45.3'}, {'value': '73.4'}]


print(max(my_list, key=lambda ele: float(ele['value'])))




