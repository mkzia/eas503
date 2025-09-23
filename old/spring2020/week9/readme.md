# Week 9 Relational Database (SQL) Continued

## Agenda
- Go over Lab1
- Go over syllabus
- Project proposal
- Lecture
- Show how database homework will work 

## Joining Tables
### Ref: https://www.diffen.com/difference/Inner_Join_vs_Outer_Join
### There are two types of joins
- Inner Join
- Outer Join
	- Left Outer Join (or Left Join)
    - Right Outer Join (or Right Join)
    - Full Outer Join (or Full Join) 
- Example in join_example_database.db

#### Inner Join

```sql
SELECT Prices.Product, Prices.Price, Quantities.Quantity
FROM Prices INNER JOIN Quantities
ON Prices.Product = Quantities.Product;

```

#### Left Join

```sql
SELECT Prices.Product, Prices.Price, Quantities.Quantity
FROM Prices LEFT OUTER JOIN Quantities
ON Prices.Product = Quantities.Product;
```

#### Right Join -- Doesn't work in SQLITE3

```sql
SELECT Prices.Product, Prices.Price, Quantities.Quantity
FROM Prices RIGHT OUTER JOIN Quantities
ON Prices.Product = Quantities.Product;
```

#### Left Join -- This works

```sql
SELECT Prices.Product, Prices.Price, Quantities.Quantity
FROM Quantities LEFT OUTER JOIN Prices
ON Quantities.Product = Prices.Product;
```

#### Full Outer join -- does not work

```sql
SELECT Prices.Product, Prices.Price, Quantities.Quantity
FROM Prices FULL OUTER JOIN Quantities
ON Prices.Product = Quantities.Product;
```

### Emulate Full outer join
- REF: https://www.sqlitetutorial.net/sqlite-full-outer-join/

```sql
SELECT Prices.Product, Prices.Price,  Quantities.Product, Quantities.Quantity
FROM Prices 
LEFT OUTER JOIN Quantities
ON Prices.Product = Quantities.Product
UNION ALL
SELECT Prices.Product, Prices.Price, Quantities.Product, Quantities.Quantity
FROM Quantities 
LEFT OUTER JOIN Prices
ON Quantities.Product = Prices.Product;
```


## Foreign Key
- What is a foreign key? In a relational database, you can relate one table to another table. The two
tables can be related if and only if both tables have one column in common. This column has to be declared as a INTEGER data type that cannot be NULL and has the `PRIMARY KEY` constraint -- example: ColumnName INTEGER NOT NULL PRIMARY KEY;
- IMPORTANT: Foreign key constraint is not enabled by default in SQLite

## SQL basic command review
- Data and commands taken from: https://www.guru99.com/sqlite-tutorial.html

### Load data
```
sqlite3 sampledata.db
```


### Inspect tables
```
.tables # show all available tabes
.schema Marks # show create statement of table
.header ON # show column names
.mode column # pretty format output
PRAGMA foreign_keys = ON # Enforce foreign_keys constraint -- OFF by default!
```

### SELECT *
```
SELECT * FROM Departments;	
SELECT * FROM Students;	
```

### SELECT * with join 
#### Method 1 -- explicitly link two tables
- Notice two department id columns!
```
SELECT * 
FROM Students
INNER JOIN Departments ON Students.DepartmentId = Departments.DepartmentId;
```

#### Method 2 -- let SQLite infers join condition -- but you specify the shared column name
- Only one column for DepartmentId
```
SELECT *
FROM Students
INNER JOIN Departments USING(DepartmentId);

SELECT Students.StudentName, Marks.Mark FROM Students JOIN Marks USING(StudentID)
```


### SELECT * with join and choose some columns
```
SELECT StudentName, DateOfBirth, DepartmentName
FROM Students
INNER JOIN Departments USING(DepartmentId);
```

### LEFT JOIN 
```
SELECT
  Students.StudentName,
  Departments.DepartmentName
FROM Students             -- this is the left table
LEFT JOIN Departments ON Students.DepartmentId = Departments.DepartmentId;
```

### Redefining Column name using alias
```
SELECT StudentName AS 'Student Name', DateOfBirth AS 'DOB', DepartmentName AS 'Department'
FROM Students
INNER JOIN Departments USING(DepartmentId);

SELECT Tests.TestName AS 'Test Name', 
count(Marks.Mark) as 'Number of Tests',
avg(Marks.Mark) AS 'Average'
FROM Marks JOIN Tests USING(TestId) GROUP BY Tests.TestId;
```

### Using a reference for table name
```
SELECT s.*
FROM Students AS s;
```

### Example without alias
```
SELECT Students.StudentName, Departments.DepartmentName
FROM Students
INNER JOIN Departments ON Students.DepartmentId = Departments.DepartmentId;
```

### Example with alias -- useful for joins -- use shorter name with joining
```
SELECT s.StudentName, d.DepartmentName
FROM Students AS s
INNER JOIN Departments AS d ON s.DepartmentId = d.DepartmentId;	
```

### Concatenation operator ||
```
SELECT 'Id with Name: '|| StudentId || ': ' || StudentName AS StudentIdWithName
FROM Students;
```


### WHERE -- case insensitive
```
SELECT StudentName FROM Students WHERE StudentName LIKE 'j%';
SELECT StudentName FROM Students WHERE StudentName LIKE '%n%';
```

### WHERE operator with multiple conditions using AND or OR operator
```
SELECT * 
FROM Students 
WHERE (StudentId > 5) AND (StudentName LIKE 'N%');


SELECT * 
FROM Students 
WHERE (StudentId > 5) OR (StudentName LIKE 'M%');
```


### BETWEEN operator
```
SELECT *
FROM Students
WHERE StudentId BETWEEN 5 AND 8;
```

### IN operator
```
SELECT * 
FROM Students
WHERE StudentId IN(2, 4, 6, 8);
```

### NOT IN operator
```
SELECT * 
FROM Students
WHERE StudentId NOT IN(2, 4, 6, 8);
```

### WHERE EXISTS operator
```
SELECT * FROM Departments;

SELECT DepartmentName
FROM Departments AS d
WHERE EXISTS (SELECT DepartmentId FROM Students AS s WHERE d.DepartmentId = s.DepartmentId);

SELECT DepartmentName
FROM Departments AS d
WHERE NOT EXISTS (SELECT DepartmentId 
                  FROM Students AS s 
                  WHERE d.DepartmentId = s.DepartmentId);

```

### ORDER BY operator
```
SELECT s.StudentName, d.DepartmentName
FROM Students AS s
INNER JOIN Departments AS d ON s.DepartmentId = d.DepartmentId
ORDER BY d.DepartmentName ASC , s.StudentName DESC;
```

### DISTINCT operator
```
SELECT d.DepartmentName
FROM Students AS s
INNER JOIN Departments AS d ON s.DepartmentId = d.DepartmentId;


SELECT Departments.DepartmentName
FROM Students
INNER JOIN Departments USING(DepartmentId);


SELECT DISTINCT d.DepartmentName
FROM Students AS s
INNER JOIN Departments AS d ON s.DepartmentId = d.DepartmentId;
```


### GROUP BY
```
SELECT d.DepartmentName, COUNT(s.StudentId) AS StudentsCount
FROM Students AS s 
INNER JOIN Departments AS d ON s.DepartmentId = d.DepartmentId
GROUP BY d. DepartmentName;
```

### An advanced query
```
SELECT 
  d.DepartmentName,
  COUNT(s.StudentId) StudentsCount,
  GROUP_CONCAT(StudentName) AS Students
FROM Departments AS d 
INNER JOIN Students AS s ON s.DepartmentId = d.DepartmentId
GROUP BY d.DepartmentName
HAVING COUNT(s.StudentId) >= 3;
```

### Handing NULL values
```
SELECT * FROM Students WHERE DepartmentId = NULL; ### This does not work! Have to use the IN operator
SELECT * FROM Students WHERE DepartmentId IS NULL;
```

### CASE operator
```
SELECT 
  StudentName,
  CASE 
    WHEN DepartmentId IS NULL THEN 'No Dept.'
    ELSE DepartmentId 
  END AS DepartmentId
FROM Students;
```

### Loading data from SELECT Query into a new table
```
CREATE TABLE [TestAvgs] (  
    [TestId] INTEGER  NOT NULL PRIMARY KEY,  
    [TestName] NVARCHAR(50)  NULL, 
    [TestAvg] REAL  NULL   
); 

INSERT INTO TestAvgs(TestId, TestName, TestAvg)
SELECT Tests.TestId, Tests.TestName 'Test Name', avg(Marks.Mark) 'Average' FROM Marks JOIN Tests USING(TestId) GROUP BY Tests.TestId;
```

### Altering Tables
- Can easily rename tables 
```
ALTER TABLE existing_table
RENAME TO new_table;
```
- Can easily add columns to tables
```
ALTER TABLE table
ADD COLUMN column_definition;
```
- Can drop a column by using select statement and saving the output to another table
- To change data type, add/remove restriction, or change column name, you have to create a new table and populate it with old data

## UPDATE and DELETE
```
UPDATE Students
SET DepartmentId = 4
WHERE StudentId = 1;
```

```
DELETE FROM Students
WHERE StudentId = 1;
```

## Using SQLite with Python
- see files 
```
sqlite_example.py
sqlite_example2.py
sqlite_example3.py
```

## Database Review and Normalization

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

