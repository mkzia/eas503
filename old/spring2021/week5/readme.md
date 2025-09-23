# Week5

## Week 5 Topics
- For loops
- Modify loop execution
- while loops
- List Comprehension
- Sets
- Dictionaries
- Lambda
- Filter
- Map
- Sorting
- Matplotlib


## Repeating code using loops

```
for <ele> in <sequence>:
	<body>
```

- The loop index variable `ele` takes on each successive value in the sequence, and the statements in the body of the loop are executed once for each value.
- For loops have a limitation -- you have to know how many times you are looping -- it is a definite loop. The number of iterations is determined when the loop starts. If you do not know how many times you will be looping, use a while loop, which is an indefinite loop that will continue to loop until its condition is no longer true.

```
while <condition>
	<body>
```

- Loop is controlled using `break` and `continue`. 


### List comprehension
- Unique to Python
- Three variations

```python
[ f(ele) for ele in sequence ]

[ f(ele) for ele in sequence if condition ]

[ f(ele) if condition else g(ele) for ele in sequence ]

```

### File Handling


```python
with open(filename, 'r') as file:
	for line in file:
		# do something with line

```


### Sets
- Formal mathematical sets
- Do not have duplicate values
- Are not ordered
- Cannot access via index. 
- useful for doing set operations

```python
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

```


### Dictionaries
- limitations of list
- list has collection of values, but no description
- student
  - name
  - email 
  - id
  - major
- dictionary
- key value pair
- key is the index
- value is the value 
- two ways to create dictionary
- my_dict = {}
- my_dict = dict()
- key value are separate colons
- key can only be string or number
- value can be anything!
- All information is stored like a dictionary, you supply the key and you get the value


```python
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
    print(False)

# # dictionary methods
my_dict.clear() ## empty dict

my_dict.copy() ## copy dict -- unique objects in memory
# # check == and is; == is for values and is for memory

# # create default dictionary with initial value
new_student = {}.fromkeys(
    ['name', 'email', 'id', 'major'], 'missing')

my_dict = {}.fromkeys(range(5), 'iammissing')

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

```

## Lambda, Filter, and Map

### Lambda
lambda a function without a name;
- anonymous functions;
- one line only;
- single expression only
- stored in a variable
- When do you use it? Pass a function into another function as a parameter
- lambda variables (comma separated): expression
- lambda functions are used with other functions. Usually with map, filter, sort

### Filter
- Uses `function` to test the truthiness of each value in the sequence and returns a filtered list.
- `function` must return True or False

```python
filter(function, sequence)
```
### Map
- Uses `function` to transform the values in a sequence 
```python
map(function, sequence)
```

