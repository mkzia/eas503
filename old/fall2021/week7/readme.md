# Week7

## Week 7 Topics
- Function Input 
- Variable Scope
- Object-Oriented Programming
- Overloading
- Iterator
- Generator


### Function (input arguments)
- no arguments
- positional/fixed/required arguments
- required arguments and optional arguments
- keyword arguments 

### Function Scope
Ref: Python for Programmers by Paul Deitel and Harvey Deitel
```
In many programming languages there are two ways to pass arguments--pass-by-value
and pass-by-reference (sometimes called call-by-value and call-by-reference, respectively):
  - With pass-by-value, the called function receives a copy of the argument's value 
  and works exclusively with that copy. Changes to the function's copy do not affect the original
  variable's value in the caller.
  - With pass-by-reference, the called function can access the argument's value in the caller
  directly and modify the value if it's mutable. 

Python arguments are ALWAYS passed by reference. SOme people call this pass-by-object-reference, 
because "everything in Python is an object." When a function call provides an argument, Python copies
the argument object's reference--not the object itself--into the corresponding parameter. This
is important for performance. Function often manipulate large objects--frequency copying them would
consume large amount of computer memory and significantly slow down program performance. 

```

- immutable: int, float, string, tuple, frozenset
- mutable: list, dict, set
- If you pass a mutable data type to a function, changes you make persist outside of the function!


### Object-Oriented Programming
- We know how to store various data in Python using various data types  
- We also know how to define functions that manipulate
or operate on that data. 
- Object-oriented programming allows us to define
the data and functions in one place.

#### Comparison between Procedural and Object-oriented Programming
- Procedural programming:
  - We write a list of nouns (data)
  - We also have a separate list of verbs (functions)
  - We leave it up to the programmer to figure out which 
  data goes with with function
- Object-oriented programming:
  - We define an object which contains both the nouns (data) and verbs (functions) that manipulate that data. 
  - Data --> Attribute
  - Function --> Method 


###### Procedural Programming Example

```python
# function 
def average(numbers): 
  return sum(numbers) / len(numbers)

# data
scores = [80, 90, 95, 92 85]

# User has to know which data to pass into function
# to get desired output
print(f'The average score is {average(scores)}.')

```


###### Object-Oriented Programming Example
- Define a new class that will contain both the
data and the function to manipulate it. 
- So put the scores list and the average function
inside a class

```python
class ScoreList():
  def __init__(self, scores):
    self.scores = scores

  def average(self):
    return sum(self.scores) / len(self.scores)

scores = ScoreList([80, 90, 95, 92 85]) 
print(f'The final score is {scores.average()}.')   
```

- No difference it the actual calculation, only that the
code is organized differently.

###### Benefits of OOP
- We can organize our code into distinct objects, so each object handles storing and manipulating the data. 
- We can create hierarchies of classes where each child
inherits from its parent class attributes and methods, reducing code repetition and improves code maintainability.


###### Thoughts on OOP
- In Python everything is an object, which means every entity has some attributes and associated functionality called methods. This means that `str` and `dict` are classes that know how to store data and how to operate on them. 
- Do not overdo OOP. It is possible to create a very large object which then basically functions like a procedural system disguised as an object-oriented one. 


#### Basic Building Blocks to defining a class
- `class` - keyword to indicate that you are creating/defining a class; example `class ScoreList`
- `__init__` - a method that is invoked automatically
when an instance of a class is created. Class is analogous to a blue print and an object is an instance
of a class with its own separate data from other objects (attributes/data), but shared functionality (methods/functions). 

```python
def __init__(self):
  pass
```

- `__repr__` - a method that returns a string containing
an object's printed representation. 

```python
def __repr__(self):
  return f'<some string >'
```

- `super()` - used to invoke parent class's methods

```python
super().__init__()
```

- `dataclasses.dataclass` - new in Python 3.7, a convenient way add common things to `__init__` and reduce redundancy. 

```python
from dataclasses import dataclass

@dataclass
class InventoryItem:
    """Class for keeping track of an item in inventory."""
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand

```

```python
def __init__(self, name: str, unit_price: float, quantity_on_hand: int = 0):
    self.name = name
    self.unit_price = unit_price
    self.quantity_on_hand = quantity_on_hand

```
- oop_example1.py
- oop_example2.py
