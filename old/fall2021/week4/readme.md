# Week4 

- Data Structures (lists, tuples)
- Repeating instructions/statements using loops


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
range(start:stop:step) # [start:step:stop)

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


- Do for loop exercises
- Do modify loop exercises
- Do while loop exercises


### File Handling


```python
with open(filename, 'r') as file:
    for line in file:
        # do something with line

```