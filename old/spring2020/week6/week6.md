# Week 6


## Topics
- Function (input parameters)
- Exception Handling
- Object Oriented Programming


### Function (input arguments)
- no arguments
- positional/fixed/required arguments
- required arguments and optional arguments
- keyword arguments 
- 


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


### OOP

#### Payroll system using polymorphism
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


#### Operator overloading
  - We know how to create objects. Now we will learn how to define what +, -, or lte means for an object
