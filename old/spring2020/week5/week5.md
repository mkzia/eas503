# Week 5


## Topics
- dict_ex5
- Lambda, Filter, and Map
- Sets
- Function (scopes and input parameters)
- Exception Handling

### What are functions and why do we need them?
  - Sometimes you have set of instructions or lines of code that is repeated in your program
    - A problem with having repeated lines of codes is that you have to maintain them at multiple locations.
    Meaning, if there is an error in your code or you want to change what those lines do, you have to update
    the code in multiple places.
    - A solution to this problem is to take the repeated lines of codes and put them inside a function.

### Scope in Python 
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


### Exception Handling

```
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