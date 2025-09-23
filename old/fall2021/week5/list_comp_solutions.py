###############################################################
# list_comp_ex1.py
# Re-write the following code to use List Comprehension
# my_list = [1, 2, 3]
# new_list = []
# for ele in my_list:
#     tmp = ele * ele
#     new_list.append(tmp)


# # list comprehension

new_list = [ele*ele for ele in my_list]


###############################################################
# list_comp_ex2.py
# Re-write the following code to use List Comprehension
# # Multiply each number by 10

# my_list = [1, 2, 3]
# new_list = []
# for ele in my_list:
#     tmp = ele * 10
#     new_list.append(tmp)

# # list comprehension

new_list = [ele*10 for ele in my_list]


###############################################################
# list_comp_ex3.py
# Upper case each letter in animal variable

# # Works with any type of sequence

animal = 'buffalo'
[char.upper() for char in animal]


###############################################################
# list_comp_ex4.py
# Title each name in the student list

students = ['john', 'jane', 'doe']

[student[0].upper()+student[1:] for student in students]


###############################################################
# list_comp_ex5.py
# Use list comprehension to get the Truthiness of each element in my_list

my_list = [0, '', []]

[bool(ele) for ele in my_list]


###############################################################
# list_comp_ex6.py
# convert each element of my_list to str using list comprehension

my_list = range(6)

[str(element) for element in my_list]


###############################################################
# list_comp_ex7.py
# use list comprehension to reduce a list of numbers to just even or odd


numbers = range(20)


# ## You can add conditional logic to list comprehension!

even = [number for number in numbers if number % 2 == 0 ]
odd = [number for number in numbers if number % 2 != 0 ]


###############################################################
# list_comp_ex8.py
# use list comprehension to modify a list of numbers such that evens are left as is
# and the odds are raised to the three power


numbers = range(10)

[number if number % 2 == 0 else number**3 for number in range(10)]


###############################################################
# list_comp_ex9.py
# use list comprehension to remove vowels from a sentence

sentence = 'I rEAlly want to gO to work'

''.join([char for char in sentence if char.lower() not in 'aeiou' and char.lower() not in 'nt'])

