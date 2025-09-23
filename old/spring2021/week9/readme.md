# Week9

## Week 9 Topics
- Object-Oriented Programming
- Database



### Object Oriented Programming
- oop_example1.py
- oop_example2.py
- Payroll system example 

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

- Demonstrate polymorphism
- operator overloading 

#### Operator overloading
- We know how to create objects. Now we will learn how to define what +, -, or lte means for an object
- add
- gt
- lt
- eq
- iterators https://www.programiz.com/python-programming/iterator
- generators https://www.programiz.com/python-programming/generator

### Self
- self.py
- class variable vs instance variable (https://www.digitalocean.com/community/tutorials/understanding-class-and-instance-variables-in-python-3)
- staticmethods vs class methods
- self is a reference to the current instance 

## Database 
- After you have parsed your data, you need to store the data 
- Databases allows you to persist data or save the data
- You can access the data later
- SQL databases support transaction or they are transactional
    - This means that the database is ACID
    - ACID - Atomic, Consistent, Isolated and Durable
    - series of operation that happen either all happen or nothing happens
    - Example: Transfer money -- decrement one account and increment another account
- We will use SQLite -- database saved as a file. Unlike flat files(csv files for example), the data stored in an optimized way so you can do queries. It is portable -- you can share your database file. Do not need to setup a database/server. It is a zero-configuration and serverless. No client/server interaction. An application will directly access the database file and read and write to it. 
    - Self-contained
    - Serverless
    - Zero-configuration
    - Transactional -- all or nothing; either all instructions are executed successfully or nothing happens. 
    - Uses dynamic types for tables -- can store any datatype in any column

- Database terminology
    - A database contains tables
    - tables store information in rows and columns
    - a relational database -- there is a relationship between two or more tables

- Use DB Browser for SQLite
- Reference: https://www.sqlitetutorial.net
- Reference: https://www.quackit.com/sqlite/tutorial
- Data: Data generated using faker
- Data: https://www.sqlitetutorial.net/sqlite-sample-database/
- Data: https://www.kaggle.com/airbnb/seattle
- https://sqlitebrowser.org/dl/

- Basic commands
`sqlite3` - start sql lite
`.help`  - list commands available
`.quit` - quit sqlite


## Load simple database
```
create table students (last_name TEXT, first_name TEXT, username TEXT, exam1 INTEGER, exam2 INTEGER, exam3 INTEGER);
.separator "\t"
.import students.tsv Students
.save student.db
.headers ON
```

## Basic commands -- Part I
```
.help
.database
.table
.schema <name_of_table>
.quit
```

### SELECT command
```
SELECT * FROM students;
SELECT username, exam1 FROM STUDENTS;
SELECT username, exam1 FROM STUDENTS ORDER BY username;
SELECT username, exam1 FROM STUDENTS ORDER BY username LIMIT 20;
SELECT username, exam1, exam2 FROM STUDENTS ORDER BY exam1 ASC LIMIT 10; 
SELECT username, exam1 FROM STUDENTS ORDER BY exam1 DESC LIMIT 10; 
```

### Save output to a file
```
.output output.txt
SELECT username, exam1 FROM STUDENTS ORDER BY -exam1 LIMIT 10; 
.output stdout
```

### Backup whole database
```
.output dump.sql
.dump
.output stdout
```

### Calculating Average
```
SELECT 
 avg(exam1) as `Exam1 Average`, avg(exam2), avg(exam3)
 FROM students;
```

### Find all exam1 grades greater than 80
```
SELECT
username, exam1
FROM
students
WHERE exam1 > 80;
```

### Find all exam1 between
```
SELECT
username, exam1
FROM
students
WHERE exam1 BETWEEN 80 and 90;
```



### Get count of exam1 greater than 80
```
SELECT
count(exam1)
FROM
students
WHERE exam1 > 80;
```

### Find students with same first name
```
SELECT
*
FROM
students
WHERE first_name == 'Melissa'
```

### Find students IN list
```
SELECT
*
FROM
students
WHERE first_name in ('Melissa', 'Stephanie', 'Alex');
```


### Find students LIKE %
```
SELECT
*
FROM
students
WHERE first_name LIKE 'Alex%';
```

### Find students LIKE  %%
```
SELECT
*
FROM
students
WHERE first_name LIKE '%ath%';
```

### Find Histogram exam1 grades using GROUP BY
```
SELECT exam1, count(exam1) as c  FROM students GROUP BY exam1 ORDER BY c DESC;
SELECT first_name, count(first_name) as name_count  FROM students GROUP BY first_name ORDER BY name_count DESC;
```


### Adding null values
```
INSERT INTO Students('exam1') VALUES ('52');
SELECT * FROM Students;
```

### Adding NOT NULL constraint
```
create table students (
    last_name TEXT NOT NULL, 
    first_name TEXT NOT NULL, 
    username TEXT NOT NULL, 
    exam1 REAL, 
    exam2 REAL, 
    exam3 REAL
);
.separator "\t"
.import students.tsv Students

SELECT * FROM Students;
.schema Students

INSERT INTO Students('exam1') VALUES ('52');

```



### Primary Key
```
.headers ON
PRAGMA foreign_keys;
PRAGMA foreign_keys = ON;
PRAGMA foreign_keys;
CREATE TABLE Teachers(
  TeacherName  TEXT NOT NULL
);

.tables
.schema Teachers

INSERT INTO Teachers ('TeacherName') VALUES ('John Smith');
SELECT * FROM Teachers;
INSERT INTO Teachers ('TeacherName') VALUES ('John Smith');


SELECT rowid, * FROM Teachers;

```

When you create a table that has an `INTEGER NOT NULL PRIMARY KEY` column, this column is the alias of the `rowid` column. It uniquely defines a record/row.

```
.headers ON
DROP TABLE Teachers;
 
CREATE TABLE Teachers (
   TeacherId INTEGER NOT NULL PRIMARY KEY,
   TeacherName  TEXT NOT NULL
);
INSERT INTO Teachers ('TeacherName') VALUES ('John Smith');
INSERT INTO Teachers ('TeacherName') VALUES ('John Smith');
SELECT * FROM Teachers;
```


### Making a teacher Unique
```
.headers ON
DROP TABLE Teachers;
 
CREATE TABLE Teachers (
   TeacherId INTEGER NOT NULL PRIMARY KEY,
   TeacherName  TEXT NOT NULL,
   TeacherEmployeeID INTEGER NOT NULL,
   UNIQUE (TeacherEmployeeID)
);
INSERT INTO Teachers ('TeacherName', 'TeacherEmployeeID') VALUES ('John Smith', 100001);
INSERT INTO Teachers ('TeacherName', 'TeacherEmployeeID') VALUES ('John Smith', 100002);
SELECT * FROM Teachers;
```
