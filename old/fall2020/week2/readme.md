# Week2

## Week 2 Topics
- Chapters 3, 4, 5  from Practical Programming 3rd Edition By Paul Gries et al.. 
- Review
- Functions -- defining your own functions
- Working with Text/Strings
- Making Choices/Flow Control/Conditionals

## Review
- Analogy: English grammar is a set of rules that tells us how to say things correctly. Put another way, if we follow the rules of English language, a person listening to us will understand our intent. Programming languages also have a set of rules that if we follow them, the computer will understand our intent and carry out our instructions. In the previous lecture, we covered some of the rules for communicating our intent to a computer, specifically using the Python programming language. 
- How do we tell Python that we want to store a value?
  - What are the rules and conventions for naming variables?
- What kinds of values can Python store?
- How do we tell Python to print what we want?
- How do we tell Python to ask us for an input and save it to a variable?
- What mathematical operators does Python understand?
- How can you tell the computer to update a variable by adding a value to the variable?  There are two ways of doing this. 

## Functions 

### Defining your own functions
- The build-in functions that Python provides do basic tasks. We can write our own functions that can execute complicated sequence
of instructions. Your functions will be made up of Python operators and built-in Python functions.

#### Designing New Functions: A Recipe
- What do you name the function?
- What are the parameters, and what types of information do they refer to?
- What calculations are you doing with that information?
- What information does the function return?
- Does it work like you expect it to? -- We will not cover in this class. 

#### Variations in functions
- No input; no output; example -- print something
- One or more input; no output; example -- print the input
- One or more input: one or more output; example -- take two numbers and return their sum
- No input; one or more output; example -- a random number

- Function Exercises 1-12



## Strings
- In Python, text is represented as a string, which is a sequence of characters (letters, digits, and symbols).
- In Python, we indicate that a value is a string by putting either single or double quotes around it.

### Operations on Strings
- `len()` -- to get length of a string
- `+` -- can add strings, but not str and type float or int
- `*` -- to repeat a string 
- `+=` -- add to another string and save value
- `int(3)`
- `float(3.4)`

### Simple examples

```python
'Aristotle'
"Issac Newton"

scientist = 'Issac Newton'
print(len(scientist))


'Alan Turning' + ' ' + 'Grace Hopper'

'NH' + 3 # This will not work. You cannot add a str and int type. 

'Four score and ' + str(7) + ' years ago'

int('0')
int('11')
int('-324')
float('-324.40')

'AT' * 5

'-' * 5

```

### Using Special Characters in Strings
- How would you put a single quote inside a string that is declared using a single quote?
- `'\\'` -- how would you print `/\/\`
- `'\n'`
- `'\''`
- `'\"'`
- `'\t'` -- useful for parsing TSV files



### Printing in Python
```python
print('abbcd', 2, 3)
```


### Getting information from the Keyboard
```python
number = input('Please enter a number: ')
```

```python
number = int(input('Please enter a number: '))
```

```python
def convert_celsius(fahrenheit):
    return (fahrenheit - 32.0) * 5.0 / 9.0    
```

```python
def convert_celsius():
    fahrenheit = float(input('Please enter temprature in fahrenheit: '))
    celsius =  (fahrenheit - 32.0) * 5.0 / 9.0  
    print('The temperature in celsius is: ', celsius) 

```

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

- Go Over: https://pyformat.info/


- String Exercises 1-9


- https://scipython.com/book/chapter-2-the-core-python-language-i/string-representation-of-integers-with-comma-separated-thousands/
```python
title = '|' + '{:^51}'.format('Cereal Yields (kg/ha)') + '|'
line = '+' + '-'*15 + '+' + ('-'*8 + '+')*4
row = '| {:<13} |' + ' {:6,d} |'*4
header = '| {:^13s} |'.format('Country') + (' {:^6d} |'*4).format(1980, 1990,
                                                                  2000, 2010)
print('+' + '-'*(len(title)-2) + '+',
      title,
      line,
      header,
      line,
      row.format('China', 2937, 4321, 4752, 5527),
      row.format('Germany', 4225, 5411, 6453, 6718),
      row.format('United States', 3772, 4755, 5854, 6988),
      line,
      sep='\n')
```


