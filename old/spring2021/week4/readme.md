# Week4

## Week 4 Topics
- Data Structures (lists, tuples)
- Repeating code using loops
- Lambda, Filter, Map


## Data Structures (lists, tuples)
- So far we have covered the following data types: `int`, `float`, and `bool`. Now we will
cover `list`, and `tuple` 
- Data types in Python can be classified as `mutable` and `immutable`. 
	- Immutable data types are: `int`, `float`, `bool`, and `tuple`
	- Mutable data types are: `list`, `dict`, and `set`
	- NOTE: Immutable data types are passed to a function using `pass-by-value`. Mutable data types are 
	passed to a function as a reference. This means that changes made to mutable data types persist outside
	of the function. 

### List
- `list` is a container for storing a sequence of values. The values can be of different type. When the values are all `int`, `float`, or `bool`, you can use special functions. 

#### List Index -- starts at 0
```python
whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
```

#### Creating a list
```python
grades = ['A', 'B', 'C', 'D', 'F']
```

#### Accessing a list
```python
grades[0]
``` 

#### Slicing a list
```python
grades[2:4]
grades[1::2]
grades[-1]
grades[::-1]
```

#### Reassigning a list
```python
grades = ['A', 'B', 'C', 'D', 'F']
grades[0] = 'a'
grades[1:2] = 'a'
grades[2:] = ['d', 'f']
```

#### Deleting from a list
```python
grades = ['A', 'B', 'C', 'D', 'F']
del grades[0]
del grades[1:3]
del grades
```

#### Concatenate lists
```python
grades1 = ['A', 'B', 'C']
grades2 = ['D', 'F']
grades = grades1 + grades2
```

#### Multiplication
```python
grades = ['A', 'B', 'C', 'D', 'F']
grades *= 3

```

#### Can store different data types
- But you will lose some processing functionality
```python
my_list = ['A', 1, 'Spam', True]
my_list2 = [['John', [55, 65, 86]], ['Jane', [70, 80, 80]]
```

#### Built-in List methods
- `len()` calculate length of list
- `max()` calculate max of list
- `min()` calculate min of list
- `sum()` calculate sum of list
- `sorted()` return a sorted list
- `list()` cast to type list -- convert tuple to list or a generator to list
- `any()` return `True` if the truthiness of any value is `True` in the list
- `all()` return `True` if the truthiness of all the values is `True` in the list

```python
numbers = [3, 4, 8, 9, 5, 6, 7, 0, 1, 2, 10, 11, 12]
len(numbers)
max(numbers)
min(numbers)
sum(numbers)
sorted(numbers)
list(numbers)
any(numbers)
all(numbers)
```
```python
booleans = [True, False, True]
any(booleans)
all(booleans)
```

```python
booleans = [True, True, True]
any(booleans)
all(booleans)
```

#### List methods (functions)
- `append()` - add an element to end of list
- `insert()` - insert an element to the list at the specified location
- `remove()` - remove the element 
- `pop()` - remove the last element in the list; also returns the value; you can save this to another variable
- `clear()` - empty the list
- `index()` - return position of first matching element
- `count()` - count the number of elements
- `sort()` - sort the list in place 
- `reverse()` - reverse the list in place


```python
grades = ['A', 'B', 'C']
grades.append('D')
grades.insert(4, 'F')
grades.remove(2)
grades.pop()
grades.index('C')
grades.count('C') # len(grades)
grades.sort()
grades.reverse()
```

#### List unpacking 
```python
a, b = [3,4]
```

### Tuples
- Tuple are just like lists except that they are immutable. Once you have created a tuple, you cannot modify it. 
- Why use them?
- faster than lists
- make code safer -- because you cannot change it
- valid keys in a dictionary


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


```python
range(start,stop,step) # (start,stop,step)

```


```python
values = [4, 10, 3, 8, -6]
for i in range(len(values)):
	print(i)

```


```python
values = [4, 10, 3, 8, -6]
for i in range(len(values)):
	print(i, values[i])

```

```python
values = [4, 10, 3, 8, -6]
for i in range(len(values)):
	print(i, values[i])

```

```python
values = [4, 10, 3, 8, -6]
for index, value in enumerate(values):
	print(index, value)

```



```python
values = [4, 10, 3, 8, -6]
for i in range(len(values)):
	values[i] = values[i] * 2

```

```python
metals = ['Li', 'Na', 'K']
weights = [6.941, 22.98976928, 39.0983]
for i in range(len(metals)):
	print(metals[i], weights[i])

```

```python
metals = ['Li', 'Na', 'K']
weights = [6.941, 22.98976928, 39.0983]
for metal, weight in zip(metals, weights):
	print(metal, weight)

```


```python
elements = [['Li', 'Na', 'K'], ['F', 'Cl', 'Br']]
for inner_list in elements:
	for item in inner_list:
		print(item)
```

```python
info = [['Isaac Newton', 1643, 1727],
	['Charles Darwin', 1809, 1882],
	['Alan Turing', 1912, 1954, 'alan@bletchley.uk']]
for item in info:
	print(len(item))
```



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