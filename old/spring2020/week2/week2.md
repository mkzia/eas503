# Week2

## Topics
- Review Syllabus
- Complete PS1
- Week 1 Review
- Strings
- Flow-Controls (Conditionals)
- Functions

## Week1 Review
- Analogy: English grammar is a set of rules that tells us how to say things correctly. Put another way, if we follow the rules of English language, a person listening to us will understand our intent. Programming languages also have a set of rules that if we follow them, the computer will understand our intent and carry out our instructions. In the previous lecture, we covered some of the rules for communicating our intent to a computer, specifically using the Python programming language. 
- How do we tell Python that we want to store a value?
  - What are the rules and conventions for naming variables?
- What kinds of values can Python store?
- How do we tell Python to print what we want?
- How do we tell Python to ask us for an input and save it to a variable?
- What mathematical operators does Python understand?
- How can you tell the computer to update a variable by adding a value to the variable?  There are two ways of doing this. 
- How does Python interpret a string?
- How do we tell Python to access a character from a string?

## Strings
  - A string in Python is a list of characters. A list stores a sequence of thing. In the case of a string, the list stores letters.
  - You can access individual characters with the the first character having index 0
  - You can declare strings using single or double quotes. 
    - Quotes inside other quotes:
      - "What's my name?"
  
  - `greet = 'Hello Bob'`
  - `greet[1]`
  - can do reverse indexing using negative numbers
    - `greet[-1]`
  - can slice strings; does not include the end position
    - `<string>[<start>:<end>:<skip>]` where start, end, and skip are ints
    - `greet[0:3]`
    - `greet[:5]`
    - `greet[5:]`
    - `greet[:]`
    - `greet[::2]`
  - Concatenate Strings --
    -     ```Python
      first_name = 'John'
      last_name = 'Doe'
      full_name = first_name + ' ' + 'Doe'
      print(full_name)
     ```
    - can multiply strings!
     
      ``` Python
      spam = 'spam'
      spam *= 3
      ```
   
  - Escape sequences or Escape characters
    - Use these to put in special characters
    - Most common ones
      - `'\\` -- how would you print `/\/\`
      - `'\n'`
      - `'\''`
      - `'\"'`
      - `'\t'` -- useful for parsing TSV files

  - Apache log example: https://www.keycdn.com/support/apache-access-log
  - Try to use packages already available online https://github.com/rory/apache-log-parser
  - String methods: https://www.w3schools.com/python/python_ref_string.asp
    - `capitalize()` Converts the first character to upper case
    - `count()` Returns the number of times a specified value occurs in a string
    - `lower()` Converts a string into lower case
    - `split()` Splits the string at the specified separator, and returns a list
    - `title()` Converts the first character of each word to upper case
    - `upper()` Converts a string into upper case

### String Formatting
  - The fastest and latest way to do string formatting is using the F-strings (https://realpython.com/python-f-strings/)
  - ``` python
    PI = 3.14159265359 
    print(f'{PI:.2f}')
    ```
  - But you have to know the other ways so you can read older code or use these ways if you have to use an older version of Python
    - ``` python
      PI = 3.14159265359 
      name = 'PI'
      print('%s is %.2f' % (name, PI))  # oldest way format specifier is <width>.<precision><type>
      print(('{0} is {1:.2f}'.format('PI', PI)) ) # older way {<index>:<format-specifier>} where the format specifier is <width>.<precision><type>
      print(f'{name} is {PI:.2f}') # newest way
      ```


## Conditionals

  - So far we have only written small programs that are a sequence of instructions. Sometimes you have to alter the sequential flow of a program to suit the needs of a particular situation.
  - When strings are compared, they are compared lexicographic, meaning strings are put into alphabetical order and uppercase comes before lowercase.
  - The conditional operator converts the conditional into a boolean, which is a basic Python data type.

### Conditional Operators
  - `==` Equal to 
  - `!=` Not equal to
  - `<` Less than
  - `>` Greater than
  - `<=` Less than or equal to
  - `>=` Greater than or equal to

  - These operators evaluate to True or False depending on the values you give them.
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

### Truthiness and Falsiness 
  - Things that are false on their own
    - `None` (basic data type)
    - `False` (basic data type)
    - Any empty sequence: `''`, `[]`, `()`
    - Any zero value: 0, 0.0
    - Anything whose `len()` returns 0
    - Empty objects
    - Everything else is True 
  - Assume `a=1` and `b=1`

### Boolean Operators
  | Boolean Operators | What it does?                                | Example       |
|----|---------------------------------------------|---------------|
| == | True if a has the same value as b           | a == b #True  |
| != | True if a does not have the same value as b | a != b #False |
| >  | True if a is greater than b                 | a > b # False |
| <  | True if a is less than b                    | a < b # False |
| >= | True if a is greater than or equal to b     | a >= b # True |
| <= | True if a is less than or equal to b        | a <= b # True |

### Logical Operators

| Operator | What it does?                                        | Example                                                                   |
|----------|------------------------------------------------------|---------------------------------------------------------------------------|
| `and`    | True if both a AND b are true (logical conjunction)  | if is_teacher and is_active:   print('You can access')                    |
| `or`     | True if either a OR b are true (logical disjunction) | if is_superuser or (is_teacher and is active):    print('You can access') |
| `not`    | True if the opposite of a is true (logical negation) | if not is_superuser:   print('You cannot access')    

### is vs ==
- in Python `==` and `is` are very similar comparators, but they are not the same!
```
a = 1
a == 1 # True
a is 1 # True
```
- The `==` operator compares if the values are the same or not. The `is` operator checks whether both the values refer to the same object or not.


## Functions

### General Information About Functions
  - Functions are subprograms -- they are a sequence of of statements that have a name
  - Functions can be executed at any point by using their name 
  - Functions remove duplicated code
  - Functions can call other functions
  - Functions can OPTIONALLY take parameters or inputs that they can use inside the function 

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