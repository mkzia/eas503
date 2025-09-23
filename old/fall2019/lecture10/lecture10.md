# Lecture 10

## Topics
- Review database
- Review Panda join
- Finish up remaining Panda topics from last week
- Start Matplotlib



## Database Review

- Why use a database?
  - Ref: https://www.bbc.co.uk/bitesize/guides/z8yg87h/revision/4
  - Data is stored efficiently; saves space
  - Because data is stored efficiently, you can access it faster; easy to search
  - Because data is stored efficiently, you can easily update and remove data
  - Easily sort and group data
- What is database normalization?
  - Ref: https://www.complexsql.com/database-normalization/
  - Ref: http://www.databasedev.co.uk/1norm_form.html
  - The purpose of database normalization is to:
    - eliminate redundant data
    - reduce complexity of data, making it easier to manage the data and make change
    - ensure logical data dependencies
- How is database normalization achieved?
  - By fulfilling five normal forms. Each normal form represents an increasingly stringent set of rules. Usually fulfilling the first three normal forms is sufficient.
  - Ref: https://www.1keydata.com/database-normalization/first-normal-form-1nf.php
- First Normal Form  (1NF): 
  1. if there are no repeating groups.
  2. all values are atomic, meaning they are the smallest meaningful value
- Second Normal Form  (2NF): 
  1. the table is in first normal form
  2. each non-key field is functionally dependent on the entire primary key
- Third Normal Form (3NF):
  1. the table is in second normal form
  2. there are no transitive dependencies

- Problems with example1
  - Repeating group of fields
  - The project and time fields are not made up of atomic values
  - Can't sort by last name
  - Can't sort by time because field is type text
  - Assumed relationship between project and time

- Analysis of example2
  - Can sort now!
  - How can you add another project?


- Analysis of example3 -- first normal form
  - Can do groups by employeeid or projectnum
  - Can sort by time
  - Can sort by name

- Analysis of example4
  - How would you update the project title for a given project? Have to edit in many places
  - Can you add a project without an employeeid?
  - How can you delete a project?

- Analysis of example5
  - second normal form

- Analysis of example 6
  - Phone number, which is a non-key field, has transitive dependency on another non-key field. 

- Analysis of example7
  - Removed transitive dependency 


## Example5 in Python
- How do you recreate the tables in python?
  - Write utility functions
    - A connection function
    - A create table function
    - A select function
    - Some insert functions

## Example5 in Pandas