# Week6

## Week 6 Topics
- Dictionaries
- Lambda
- Filter
- Map
- Sorting
- Python Errors
- Exception Handling
- Matplotlib

### Dictionaries
- Examples

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

### Python Errors
```python
# SyntaxError -- invalid Python syntax
def func(()):
   pass

for index in some_list
    print(index)


# NameError -- using a variable before it has been defined

def func():
   print(variable)


# TypeError -- mismatch data type

'3' + 3

# IndexError
my_list = [1, 2, 3]
my_list[4]

# ValueError calling a built-in function with invalid value type

int('3')
int('3a')

# KeyError -- like by index error for lists

student = {'username': 'john', 'grade': 50}

student['class']

# AttributeError -- missing attribute -- variables or methods

class TestClass:
    class_variable1 = 2


print(TestClass.class_variable1)
print(TestClass.class_variable2)

string = 'test1234'
string.upper()

x = [1,2,3]
x.upper()

# More @ https://docs.python.org/3/library/exceptions.html


# Raising error -- with a message or without message

raise ValueError('a message')
raise ValueError


def calculate_bmi(height, weight):

    if type(height) not in [float, int]:
        raise TypeError('Height has to be float or an int')

    if type(weight) not in [float, int]:
        raise TypeError('Weight has to be float or an int')


    if height <= 0:
        raise ValueError('Height cannot be less than or equal to 0')

    if weight <= 0:
        raise ValueError('Weight cannot be less than or equal to 0')

    return 703 * weight / height**2

```

### Exception Handling

```python
try:
    statements              # Run this main action first
except name1:
    statements              # Run if exception name1 is raised during try block
except (name2, name3):
    statements              # Run if any of these exceptions occur
except name4 as var:
    statements              # Run if exception name4 is raised, assign instance raised to var
except:
    statements              # Run for all other exceptions raised
else:
    statements              # Run if no exception was raised during try block
finally:
    statements              # Always run
```


```python
while True:
    try:
        height = float(input('Please enter height: '))
        weight = float(input('Please enter weight: '))
    except Exception as error:
        print(error)
        print('Please enter a number')
    else:
        print('I run when there is no error')
        break
    finally:
        print('I always run!')

print(calculate_bmi(height, weight))


# Try and Except blocks -- a way to handle errors
# When you raise an error, your program exits. What
# you rather want to do is to catch that error and give
# user feedback.



student = {'username': 'john', 'grade': 50}


def get_key(some_dict, key, default_value=None):
    try:
        return some_dict[key]
    except KeyError:
        return default_value


print(get_key(student, 'username1', default_value='Error'))
print(get_key(student, 'username1'))


# try, except, else, finally

## Combining exceptions

filename = 'abcd.txt'
try: 
    file = open(filename) 
except OSError: 
    print('OS error') 
except FileNotFoundError: 
    print('File not found') 

```

