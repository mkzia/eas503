# Part 1 List

# double each number

my_list = [1, 2, 3]
new_list = []
for ele in my_list:
    tmp = ele * ele
    new_list.append(tmp)

# # list comprehension

new_list = [ele*ele for ele in my_list]


# # Multiply each number by 10

my_list = [1, 2, 3]
new_list = []
for ele in my_list:
    tmp = ele * 10
    new_list.append(tmp)

# # list comprehension

new_list = [ele*10 for ele in my_list]


# # Works with any type of sequence

animal = 'buffalo'
[char.upper() for char in animal]

students = ['john', 'jane', 'doe']

[student[0].upper()+student[1:] for student in students]
new_list = []
for student in students:
    tmp = student
    new_list.append(student.title())

[bool(ele) for ele in [0, '', []]]

numbers = list(range(6))

[str(str) for str in numbers]
str(1)

# ## You can add conditional logic to list comprehension!

numbers = range(20)

even = [number for number in numbers if number % 2 == 0 ]
odd = [number for number in numbers if number % 2 != 0 ]

[number if number % 2 == 0 else number**3 for number in range(10)]

# if number % 2 == 0:
#     number
# else:
#     number = number**3

# number if number % 2 == 0 else number**3


## removing vowels

sentence = 'I really want to go to work'

''.join([char for char in sentence if char.lower() not in 'aeiou' and char.lower() not in 'nt'])


# Dictionaries
# student
#     - name
#     - email
#     - id
#     - major


# Most people use this
my_dict = {
    'name': 'john',
    'email': 'john@email.com',
    'id': 1234,
    'major': 'Engineering'
}

# Can also do this
my_dict = dict(
    name='john',
    email='john@email.com',
    id=1234,
    major='Engineering'
)


## accessing value
key = 'name'
my_dict['name']
my_dict[key]

# ## iterating over dictionaries

for value in my_dict.values():
    print(value)

for key in my_dict.keys():
    print(key)

## access both
for key, value in my_dict.items():
    print(f'key is {key} and value is {value}')

# ## test if dict contains a key

if key in my_dict:
    print(True)
else:
    print(False)

## test if dict contains a value
# default is testing in key
value = 'john'
if value in my_dict.values():
    print(True)
else:
    print(True)

# # dictionary methods
my_dict.clear() ## empty dict

my_dict.copy() ## copy dict -- unique objects in memory
# # check == and is; == is for values and is for memory

# # create default dictionary with initial value
new_student = {}.fromkeys(
    ['name', 'email', 'id', 'major'], 'missing')

my_dict = {}.fromkeys(range(5), 'missing')

# ## get
my_dict.get('name', None) # default
my_dict.get('name', False)
my_dict.get('name', 'defaultname')


# ## pop remove value using key
my_dict.pop('name')

# ## update -- way to append to dictionary
my_dict.update({'year':2010, 'ear': 2030})


# ## dictionary comprehension
# {___:___ for ___ in ___}

# my_dict = {}.fromkeys(range(5), 5)

# {key: key*value for key, value in my_dict.items()}
# {num: num*num for num in range(5)}

list1 = ['john', 'jane', 'doe']
list2 = [95, 99, 98]

{list1[i]: list2[i] for i in range(len(list1))}

dict(zip(list1,list2))


{num: ("even" if num % 2 == 0 else "odd") for num in range(1, 20)}


A = {0, 2, 4, 6, 8};
B = {1, 2, 3, 4, 5};

# 2 in A

# # union -- all values
A | B

# # intersection -- shared values
A & B

# # difference -- order matters
A - B
B - A

# # symmetric difference  https://en.wikipedia.org/wiki/Symmetric_difference
A ^ B

my_list = [1, 1, 2, 3]
my_list = list(set(my_list))


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




