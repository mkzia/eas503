# Week 3


## Topics
- Data Structures (lists, tuples, dictionaries, sets)
- Loops
- File Handling
- Function Scopes Part 

## Data Structures
- So far we have covered the following data types: `int`, `float`, and `bool`. Now we will
cover `list`, `tuple`, `dict`, and `set`. 
- Data types in Python can be classified as `mutable` and `immutable`. 
	- Immutable data types are: `int`, `float`, `bool`, and `tuple`
	- Mutable data types are: `list`, `tuple`, `dict`, and `set`
	- NOTE: Immutable data types are passed to a function using `pass-by-value`. Mutable data types are 
	passed to a function as a reference. This means that changes made to mutable data types persist outside
	of the function. 

### List
- `list` is a container for storing a sequence of values. The values can be of different type. When the values are all `int`, `float`, or `bool`, you can use special functions. 

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

#### Built-in List Functions
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
- `count()` - return the number of elements in the list
- `sort()` - sort the list in place 
- `reverse()` - reverse the list in place


```python
grades = ['A', 'B', 'C']
grades.append('D')
grades.insert(4, 'F')
grades.remove(2)
grades.pop()
grades.index('C')
grades.count() # len(grades)
grades.sort()
grades.reverse()
```

#### List unpacking 
```python
a, b = [3,4]
```

###


#### List comprehension
  - unique to Python
```
[ ___ for ___ in ___]
```

### Tuples
- Tuple are just like lists except that they are immutable. Once you have created a tuple, you cannot modify it. 
- Why use them?
- faster than lists
- make code safer -- because you cannot change it
- valid keys in a dictionary

### Sets
- Formal mathematical sets
- Do not have duplicate values
- Are not ordered
- Cannot access via index. 
- useful for doing set operations


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


## Loop
  ```
  for <var> in <sequence>:
    <body>
  ```
  - The loop index variable `var` takes on each successive value in the sequence, and the statements in the body of the loop are executed once for each value.
  - For loops have a limitation -- you have to know how many times you are looping -- it is a definite loop. The number of iterations is determined when the loop starts. If you do not know how many times you will be looping, use a while loop, which is an indefinite loop that will continue to loop until its condition is no longer met.
  ```
  while <condition>
    <body>
  ```



## Scope in Python 
  - Remember variables, which can be an int, float, string, or list, are containers for holding data
  - Where these variables can be referenced, meaning used, in your program is called `scope`
  - Since each function is its own little subprogram, the variables that are used inside one function cannot be referenced inside
  another function. This idea that a variable inside one function cannot be used inside another function is called called `scope`, 
  the scope of a variable is the limit or boundaries inside which it can be used. Variables created/declared inside a function 
  are called `local`, meaning they are local to that function. Variables that can be referenced by multiple functions are called `global`.
  - How do you pass variables between functions? You can pass them as parameters or inputs to the function. 
  - Variables in Python are of two types with respect to whether a function can change them or not and this change is preserved outside the function:
    - Immutable: `int`, `float`, `str`, `bool`, `tuple` (a tuple is a list that cannot be changed once declared)
    - Mutable: `list`, `dict`
  - When you pass mutable variables to a function and make changes inside the function, the variable preserves the changes made inside the function
  - When you pass immutable variables to a function and make changes inside the function, the variable is not changed outside the function 
  - How can you change an immutable variable? 
    - You pass an immutable variable, make changes the local copy inside the function, return the value, and set the output of the function to the variable. 
    - Return values are the main way to send information from a function back to the part of the program that called the function. 
  - NOTE: Strings are immutable and lists are mutable