# Week 7


## Topics
- Object Oriented Programming (con't)
- Introduction to SQL


### Object Oriented Programming (con't)
  - oop_example2.py
  - self.py
      - class variable vs instance variable (https://www.digitalocean.com/community/tutorials/understanding-class-and-instance-variables-in-python-3)
      - staticmethods vs class methods
      - self is a reference to the current instance 
  - Payroll system example 
    - Demonstrate polymorphism
  - operator overloading 
    - We know how to create objects. Now we will learn how to define what +, -, or lte means for an object
    - add
    - gt
    - lt
    - eq
  - iterators https://www.programiz.com/python-programming/iterator
  - generators https://www.programiz.com/python-programming/generator

#### Payroll system using polymorphism

  - Employee -- Abstract
  - variables (properties)
    - lastname
    - firstname
    - social_security_number
  - functions (methods)
    - __repr__ - - update for each class!!!
    - earnings() -- 
  - SalariedEmployee -- inherits from Employee
      - variables
        - weekly salary
      - earnings()
        - weekly salary
      - __repr__
  - HourlyEmployee -- inherits from Employee
      - variables
        - hourly_wage
        - hours_worked
      - earnings()
        - hourly wage * hours worked
        - rate is 1.5 over 40 
      - __repr__
  - CommissionEmployee -- inherits from Employee
      - variables
        - sales
        - rate
      - earnings()
        - sales * rate
      - __repr__
  - BasePlusCommissionEmployee -- inherits from CommissionEmployee
      - variables
        - sales
        - rate
      - earnings()
        - sales * rate + salary
      - __repr__



