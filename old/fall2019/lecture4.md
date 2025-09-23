# Week 4

## Boolean and Conditional Logic Review
  - Conditionals are used to instruct computer to make a decision. 
  ```Python
  if some condition is True:
    do something
  elif some other condition is True: # else if 
    do something
  elif some other condition is True: # else if 
    do something
  elif some other condition is True: # else if 
    do something
  else:
    do something 
  ```
  - colons are important and indentation matters
  - can have many elif tests
  - do not need else
  - conditions can be nested
  ## Truthiness and Falsiness 
  - Things that are false on their own
    - `None` (basic data type)
    - `False` (basic data type)
    - Any empty sequence: `''`, `[]`, `()`
    - Any zero value: 0, 0.0
    - Anything whose `len()` returns 0
    - Empty objects
    - Everything else is True 
  - Assume `a=1` and `b=1`

## Boolean Operators
  | Boolean Operators | What it does?                                | Example       |
|----|---------------------------------------------|---------------|
| == | True if a has the same value as b           | a == b #True  |
| != | True if a does not have the same value as b | a != b #False |
| >  | True if a is greater than b                 | a > b # False |
| <  | True if a is less than b                    | a < b # False |
| >= | True if a is greater than or equal to b     | a >= b # True |
| <= | True if a is less than or equal to b        | a <= b # True |

## Logical Operators

| Operator | What it does?                                        | Example                                                                   |
|----------|------------------------------------------------------|---------------------------------------------------------------------------|
| `and`    | True if both a AND b are true (logical conjunction)  | if is_teacher and is_active:   print('You can access')                    |
| `or`     | True if either a OR b are true (logical disjunction) | if is_superuser or (is_teacher and is active):    print('You can access') |
| `not`    | True if the opposite of a is true (logical negation) | if not is_superuser:   print('You cannot access')    

## is vs ==
- in Python `==` and `is` are very similar comparators, but they are not the same!
```
a = 1
a == 1 # True
a is 1 # True
```

```
a = [1, 2, 3]
b = [1, 2, 3]
a == b # True -- checks to see both lists have the same elements
a is b # False -- checks to see if a is stored in the same memory location as b; hex(id(a)) and hex(id(b)) to print memory location   
c = b
b is c # True because they are no pointing to the same variable in memory
```


## Object Oriented Programming (OOP)
  - OOP is hard to learn and teach, so do not worry if you do not get it the first time. Give it some time
  - OOP is a paradigm shift in the way you think about writing your code
  - OOP can be used to define new types. You already know about types such as strings and floats. 

## What is OOP?
  - OOP allows you to represent or model things in the real world
    - e.g., a student or a car 
  - Class -- a blueprint for objects
    - classes can contain functions (methods) and variables/data 
      - in OOP functions are called methods
      - in OOP variables/data are called attributes
    - Example -- Student -- every student has a name, email, list of grades
  - Object -- a specific instance of the class; 
  - Definitions:
    - Object is an active data type that knows stuff and can do stuff:
      - a collection of related information
      - a set of operations to manipulate that information 
    - Instance Variable: the information stored inside the object 
    - Methods: operation functions that "live" inside the object 
    - In Python, Instance variables and methods together are called attributes. 

## Why OOP?
  - It helps you organize your code into logical, hierarchical groupings using classes. 
