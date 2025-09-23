# Week 5

## Resources
  - https://www.programiz.com/python-programming

## Topics
  - List comprehension
  - Dictionaries
  - Tuples
  - Sets
  - OOP programming
    - Payroll system example 
      - Demonstrate polymorphism
    - operator overloading
      - add
      - gt
      - lt
      - eq
    - iterators https://www.programiz.com/python-programming/iterator
    - generators https://www.programiz.com/python-programming/generator
    


## List comprehension
  - unique to Python
```
[ ___ for ___ in ___]
```

## Dictionaries
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

  ## Tuples
  - Why use them?
    - faster than lists
    - make code safer -- because you cannot change it
    - valid keys in a dictionary
  
  ## Sets
  - Formal mathematical sets
  - Do not have duplicate values
  - Are not ordered
  - Cannot access via index. 
  - useful for doing set operations

## OOP

### Payroll system using polymorphism
 - Employee -- Abstract
  - variables (properties)
    - lastname
    - firstname
    - social_security_number
  - functions (methods)
    - __repr__ -- 
    - earnings() -- 
 - SalariedEmployee -- inherits from Employee
 - CommissionEmployee -- inherits from Employee
 - HourlyEmployee -- inherits from Employee
 - BasePlusCommissionEmployee -- inherits from CommissionEmployee


### Operator overloading
  - We know how to create objects. Now we will learn how to define what +, -, or lte means for an object

