# Week 3

## Back to Functions

### What are functions and why do we need them?
  - Sometimes you have set of instructions or lines of code that is repeated in your program
    - A problem with having repeated lines of codes is that you have to maintain them at multiple locations.
    Meaning, if there is an error in your code or you want to change what those lines do, you have to update
    the code in multiple places.
    - A solution to this problem is to take the repeated lines of codes and put them inside a function.

## Chapter 7 -- Conditionals
  - So far we have only written small programs that are a sequence of instructions. Sometimes you have to alter the sequential flow of a program to suit the needs of a particular situation.
  - When strings are compared, they are compared lexicographic, meaning strings are put into alphabetical order and uppercase comes before lowercase.
  - The conditional operator converts the conditional into a boolean, which is a basic Python data type.


## Chapter 8 -- Loop
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
