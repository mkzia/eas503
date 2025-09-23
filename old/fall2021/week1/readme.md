# Week1

## Week 1 Topics
- Chapters 1, 2, 3, 4, 7 from Practical Programming 3rd Edition By Paul Gries et al.. 
- Course Introduction
- Python Basics (Data types, mathematical operations, variables)
- Functions
- Manipulating Strings
- NBGrader 

## Introduction
  - Take attendance
  - Go over syllabus
  - Survey class about programming experience and OS
  - Accessing Python
    - use `Ipython` from command-line
    - use `spyder` from Anaconda GUI
    - use `notebook` from Anaconda GUI
  - Sublime -- a good editor 
  - General Features of Python
    - Interpreted language
    - Forced indentation
    - Easy to use and learn syntax. Good first programming language
    - Very popular in data science field along with R

## Command Line Basics
  - organization: folders inside folders
  - absolute path vs relative path;
  - Using `~`
  - `pwd` -- Print name of current/Working Directory
  - `cd` -- Change Directory
  - `ls` -- list directory contents
  - `rm` -- remove directory entries; delete files and folders
  - `cp` -- copy files or folders
  - `mkdir` -- create new directory; `-p` option
  - `touch` -- change file access and modification times, but can     also be used to create a new file
  - `python test.py` -- running a program from command line
  - `python test.py > log.txt` -- saving output from program to command line


## Programs and Programming

- Programming teaches you how to make computers do what you want them to do. 
- A program is a set of detailed step-by-step instructions to a computer. It is written in terms of a few basic operations that its reader already understands. Using these few basic operations, you can "teach" a computer new operations by defining them in terms of the basic operations.
  - Example: Computers understand the addition and division operator, which are the basic mathematical operators. You can teach the 
  computer to calculate the average by using the addition and division operator by instruction the computer to add all the numbers in a sequence and divide by the size of the sequence. 
  - You can then use the new average operation and combine with other operations to create more operations. It’s a lot like creating life by putting atoms together to make proteins and then combining proteins to build cells, combining cells to make organs, and combining organs to make a creature.
  Defining new operations and combining them to do useful things is the heart and soul of programming.

## What is a Programming Language?
- You can express directions to the nearest bus station in many different languages such as English, Spanish, or Hindi. 
- Similar to natural languages, there are many programming languages. But they all are instructions that a machine
can understand. Programming languages can also look different. For example `3 + 4` in Python means add three to four. This same
instruction in Schema is express as `(+ 3 4)`.  They are both express the same idea-- they just look different. 
- Every programming language has a way to write mathematical expressions,
repeat a list of instructions a number of times, choose which of two instructions
to do based on the current information you have, and much more.

## What does a programming language do?
- It takes a high-level human readable language expression such as `c = a + b` and translates to machine language that the computer can execute.
- Compilers convert programs written in a high-level language into the machine language of some computer.
- Interpreters simulate a computer that understands a high-level language.
- The source program is not translated into machine language all at once.
- An interpreter analyzes and executes the source code instruction by instruction (line-by-line).
- Compiling vs. Interpreting
- Once program is compiled, it can be executed over and over without the source code or compiler. If it is interpreted, the source code and interpreter are needed each time the program runs
- Compiled programs generally run faster since the translation of the source code happens only once.
- Interpreted languages are part of a more flexible programming environment since they can be developed and run interactively
- Interpreted programs are more portable, meaning the executable code produced from a compiler for a Pentium won’t run on a Mac, without recompiling. If a suitable interpreter already exists, the interpreted code can be run with no modifications.

## Ambiguity in Language 
- Natural Language can have ambiguity. 
- English example: "I saw a man on a hill with a telescope."
  - There’s a man on a hill, and I’m watching him with my telescope.
  - There’s a man on a hill, who I’m seeing, and he has a telescope.
  - There’s a man, and he’s on a hill that also has a telescope on it.
  - I’m on a hill, and I saw a man using a telescope.
  - There’s a man on a hill, and I’m sawing him with a telescope.
  - source: https://www.quora.com/What-are-some-examples-of-ambiguous-sentences

- <strong>Bad code can be ambiguous due to human error. To the machine it is not ambiguous.</strong> When this happens, the program might behave unexpectedly. This unexpected behavior is called a bug!


## Syntax, Expressions, Values, Operators, and Operands 
- The `syntax` of a computer language is the set of rules that defines the combinations of symbols that are considered to be correctly structured (Wiki).
- An `expression` is a syntactic entity in a programming language that may be evaluated to determine its value (Wiki).
- `2 + 2` 
  - `2` is a value
  - `+` is an operator
  - `2` is a value
  - `2 + 2` is an expression because it expresses the intent of the programmer in a syntax that Python understands.
  - the value and the operator are combined or reduced to 4 -- i.e., the expression 2 + 2 is `evaluated` to 4. In this
  expression, 2 is also called an operand, i.e., the data that is manipulated (Wiki) using operators. 
- Expressions do not have to involve an operator. 
- When an expression is evaluated, it produces a single value. 

## Basic Data Types
- Every value in Python has a particular type, and the types of values determine how they behave when they are combined. 
- You will mostly use these data types: `int`, `float`, `str`, `True/False`, and `None`

## Operators
- `+` Addition -- `2+2=4`
- `-` Subtraction -- `5-2=3`
- `*` Multiplication -- `2*3=6`
- `/` Division -- `12/6=2`
- `**` Exponentiation - raise number to a given power; `2 ^ 3` or `2 * 2 * 2`
  - `64 ** 0.5` is allowed
- `%` Modulo -- remainder operator. Good for figuring out if a number is even or odd
- `//` integer division (i.e. quotient without remainder) `10//3 = 3`

## Operator Notes
- 3/4 is a float in Python! Other languages would cut off the decimal
- By default division results in a float

## Numbers
- Python has the following number data types:
  - int - whole number, positive or negative, unlimited
  - float - number with decimals, positive or negative
  - complex - `7+3j`
- Ints vs Floats
  - Stored differently
  - Floats take up a set amount of space. Ints take up variable amount of space. Ints are stored as bignum data type behind the scenes. 
  
  ```python
  import sys
  sys.getsizeof(2.0)
  Out[3]: 24
  sys.getsizeof(2**30)
  Out[4]: 32
  sys.getsizeof(2**130)
  Out[6]: 44
  ```

  - Ints and floats both can have positive and negative
  - `type()` -- used to figure out which type of data type it is
- Why use ints? 
  - The underlying algorithms that perform computer arithmetic are simpler, and can therefore be faster for ints than the more general algorithms required for float values. Maybe not the case anymore?
- Float can only represent approximations to real numbers
  - `2/3` vs `1/3`
- If you do not need fraction values, use int.

## Operator Precedence
- PEMDAS - use parenthesis to manipulate the order in which things are calculated 
  - what is `8/2(2+2)`?
- Precedence
  - Parenthesis
  - Exponentiation
  - Negation
  - Multiplication, division, integer division, and remainder
  - Addition and subtraction
- `212 - 32 * 5 / 9` What is wrong with this expression?



## Working with large numbers
- 10000000000 + 0.00000000001
- The result ought to have twenty zeros between the first and last significant digit, but
that’s too many for the computer to store, so the result is just 10000000000—it’s as if
the addition never took place. Adding lots of small numbers to a large one can
therefore have no effect at all, which is not what a bank wants when it totals up the
values of its customers’ savings accounts.
- If you have to add up floating-point numbers, add them from smallest
to largest in order to minimize the error.

#### Identifiers, Naming Variables in Python, Remembering Values
- Variables give names to values (number, string, or boolean); Technically they are called identifiers. They are a container of information that a computer program will manipulate using a sequence of instructions. 
- Variables names MUST follow certain rules and it is BEST to follow Python guidelines for naming 
- Restrictions for identifiers or naming things in Python
  1. Start with letter or underscore
  2. The rest can have letters, underscore, and numbers
  3. symbols cannot be used in name (@,+)
  4. Don't use Python keywords or reserved words such as `print`, `str`, `int`, `float`
    - `int = 3` do `del int` to restore python keyword
    - `print = Yah` do `del print` to restore Python keyword
- Conventions for identifiers or naming things in Python
  1. use snake_case not camelCase
  2. variables should be lowercase
  3. upper case are used for constants PI = 3.14
  4. UpperCamelCase for classes
  5. `__private__`  double underscore is convention that means you are not supposed access this variable directly. They are by convention like private variables in other languages. 

#### Working with Variables
- `x = 503`;  
- `y = "EAS503"`
- `print(x)`
- `print(y)`
- `y = 34` this is allowed because you can reassign value of a variable with the new value having a different data type in Python;
This is called Dynamic typing;  C++ statically-typed -- cannot change the variable type. Define variable and variable definition will be enforced
- `x = 3.9 * x * (1 - x)`
- `x = 10`
- `x = 11`
  - A variable in Python is like a sticky note on a value. When you change the variable, the sticky note changes to a different value. The variable simply switches to refer to the new value. The old value is not erased immediately. Python has automatic garbage collection.
- `name = input("What is your name? ")` -- used to prompt user for input; the `name` variable will be a <strong>string!</strong>
  - avoid using `eval` for type casting, meaning changing type of variable from one type to another.
- `sum, diff = x+y, x-y` -- simultaneous assignment 
  - useful when you want to swap values
    - So instead of doing this:

    ``` Python
      temp = x
      x = y
      y = temp
    ```
   -  do:
      - `x, y = y, x`


- `+=` - `x += 3` is the same as `x = x + 3`
- `-=` - `x -= 3` is the same as `x = x - 3`
- `*=` - `x *= 3` is the same as `x = x * 3`
- `/=` - `x /= 3` is the same as `x = x / 3`



## Functions
- What is a function? https://www.mathsisfun.com/sets/function.html
- Functions are subprograms -- they are a sequence of of statements that have a name
- Functions can be executed at any point by using their name 
- Functions remove duplicated code
- Functions can call other functions
- Functions can OPTIONALLY take parameters or inputs that they can use inside the function 

### Built-in functions
- `abs(-9)` -- `-9` is the input argument. Arguments appear between the parenthesis after the function name

```
day_temperature = 3
night_temprature = 10
abs(day_temperature - night_temprature)
```

Because function calls produce values, they can be used in expressions:

```
abs(-7) + abs(3.3)
```

Functions to convert one type of variable to another
```
int(34.6)
int(-4.3)
float(21)
str(21)
```

The Round function can round floats
```
round(3.8)
round(3.3)
round(3.5)
round(-3.3)
round(-3.5)
```

The round function can take an OPTIONAL second argument

```
round(3.141592653,2)
```

The `help(fxn)` function gives information about a function

```
help(round)
help(pow)
```

Using the `pow` function
```
pow(2, 4)
pow(2, 4, 3)
```

We can also use function calls as arguments to other functions:

```
pow(abs(-2), round(4.3))
```

You can use the `id()` function to find the memory address of objects. 

```
id(-9)
id(23.1)
shoe_size = 8.5
id(show_size)
```

Some other useful functions
```
min(2, 3, 4)
max(2, -3, 4, 7, -5)
max(2, -3, min(4, 7), -5)

```

### Defining your own functions
- The build-in functions that Python provides do basic tasks. We can write our own functions that can execute complicated sequence
of instructions. Your functions will be made up of Python operators and built-in Python functions.

#### Designing New Functions: A Recipe
- What do you name the function?
- What are the parameters, and what types of information do they refer to?
- What calculations are you doing with that information?
- What information does the function return?
- Does it work like you expect it to? -- We will not cover in this class. 


```python
def f(x):
    squared_x  = x * x
    return squared_x
```

```python
def f(x):
    squared_x = x ** 2
    return squared_x
```

```python
def f(x):
    squared_x = pow(x, 2)
    return squared_x
```

```python
def f(x):
    return x**2
```

```python
def f(x):
    return pow(x, 2)
```


#### Variations in functions
- No input; no output; example -- print something
- One or more input; no output; example -- print the input
- One or more input: one or more output; example -- take two numbers and return their sum
- No input; one or more output; example -- a random number
- Function Exercises 1-12
