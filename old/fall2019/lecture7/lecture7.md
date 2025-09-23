# Week 7 Relational Database (SQL)
- After you have parsed your data, you need to store the data 
- Database allows you to persist data or save the data
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

- Basic commands
`sqlite3` - start sql lite
`.help`  - list commands available
`.quit` - quit sqlite


## Load simple database
```
create table students (last_name TEXT, first_name TEXT, username TEXT, exam1 REAL, exam2 REAL, exam3 REAL);
.separator "\t"
.import students.tsv Students
.save student.db
.headers ON
```

## Basic commands
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

### Find students with same last name
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

When you create a table that has an `INTEGER PRIMARY KEY` column, this column is the alias of the `rowid` column.

```
.headers ON
DROP TABLE Teachers;
 
CREATE TABLE Teachers (
   TeacherId INTEGER PRIMARY KEY,
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
   TeacherId INTEGER PRIMARY KEY,
   TeacherName  TEXT NOT NULL,
   TeacherEmployeeID INTEGER NOT NULL,
   UNIQUE (TeacherEmployeeID)
);
INSERT INTO Teachers ('TeacherName', 'TeacherEmployeeID') VALUES ('John Smith', 100001);
INSERT INTO Teachers ('TeacherName', 'TeacherEmployeeID') VALUES ('John Smith', 100002);
SELECT * FROM Teachers;
```


### Create relationship
```
PRAGMA foreign_keys;
PRAGMA foreign_keys = ON;
PRAGMA foreign_keys;

.headers ON
DROP TABLE Teachers;
 
CREATE TABLE Teachers (
   TeacherId INTEGER PRIMARY KEY,
   TeacherName  TEXT NOT NULL,
   TeacherEmployeeID INTEGER NOT NULL,
   UNIQUE (TeacherEmployeeID)
);

CREATE TABLE Courses(
  CourseId     INTEGER PRIMARY KEY, 
  CourseName   TEXT NOT NULL,
  CourseShortID   TEXT NOT NULL,
  TeacherId INTEGER NOT NULL,
  FOREIGN KEY(TeacherId) REFERENCES Teachers(TeacherId),
  UNIQUE (CourseName, CourseShortID)
);

INSERT INTO Teachers (TeacherName, TeacherEmployeeID)
VALUES ('Melissa Larson', 10001);

INSERT INTO Teachers (TeacherName,TeacherEmployeeID)
VALUES ('Christopher Smith', 10002);

INSERT INTO Courses (CourseName, CourseShortID, TeacherId)
VALUES ('Introduction to Python', 'EAS503', 1);

INSERT INTO Courses (CourseName, CourseShortID, TeacherId)
VALUES ('Introduction to Probability', 'EAS506', 2);


```


### Joining
```
PRAGMA foreign_keys;
PRAGMA foreign_keys = ON;
PRAGMA foreign_keys;

.headers ON
DROP TABLE Teachers;
DROP TABLE Courses;
CREATE TABLE Teachers (
   TeacherId INTEGER PRIMARY KEY,
   TeacherName  TEXT NOT NULL,
   TeacherEmployeeID INTEGER NOT NULL,
   UNIQUE (TeacherEmployeeID)
);

CREATE TABLE Courses(
  CourseId     INTEGER PRIMARY KEY, 
  CourseName   TEXT NOT NULL,
  CourseShortID   TEXT NOT NULL,
  TeacherId INTEGER NOT NULL,
  FOREIGN KEY(TeacherId) REFERENCES Teachers(TeacherId)
  åUNIQUE (CourseName, CourseShortID)
);

INSERT INTO Teachers (TeacherName, TeacherEmployeeID)
VALUES ('Melissa Larson', 10001);

INSERT INTO Teachers (TeacherName,TeacherEmployeeID)
VALUES ('Christopher Smith', 10002);

INSERT INTO Courses (CourseName, CourseShortID, TeacherId)
VALUES ('Introduction to Python', 'EAS503', 1);

INSERT INTO Courses (CourseName, CourseShortID, TeacherId)
VALUES ('Introduction to Probability', 'EAS506', 2);

SELECT t.TeacherName, c.CourseName, c.CourseShortID
FROM Teachers as t
    INNER JOIN Courses as c
    ON t.TeacherId = c.TeacherId;
```

### Multiple Joining

```
DROP TABLE Colors
DROP TABLE MakeModels
DROP TABLE Cars

CREATE TABLE Colors (
   color_id INTEGER PRIMARY KEY,
   color  TEXT NOT NULL,
   UNIQUE (color)
);

CREATE TABLE MakeModels (
  make_model_id     INTEGER PRIMARY KEY, 
  Make   TEXT NOT NULL,
  Model   TEXT NOT NULL,
  Year INTEGER NOT NULL,
  UNIQUE (Make, Model)
);

CREATE TABLE Cars (
   car_id INTEGER PRIMARY KEY,
   make_model_id INTEGER NOT NULL,
   color_id INTEGER NOT NULL,
   available INTEGER NOT NULL,
   FOREIGN KEY(make_model_id) REFERENCES MakeModels(make_model_id),
   FOREIGN KEY(color_id) REFERENCES Colors(color_id)
);

INSERT INTO Colors (color) VALUES ('Red');
INSERT INTO Colors (color) VALUES ('Blue');
INSERT INTO Colors (color) VALUES ('Green');

INSERT INTO MakeModels (Make, Model, Year) VALUES ('Ford', 'Explorer', 2019);
INSERT INTO MakeModels (Make, Model, Year) VALUES ('Toyota', 'Camry', 2010);
INSERT INTO MakeModels (Make, Model, Year) VALUES ('Honda', 'Accord', 2015);

INSERT INTO Cars (make_model_id, color_id, available) VALUES (1, 1, 1);
INSERT INTO Cars (make_model_id, color_id, available) VALUES (2, 1, 1);
INSERT INTO Cars (make_model_id, color_id, available) VALUES (3, 1, 1);
INSERT INTO Cars (make_model_id, color_id, available) VALUES (1, 2, 0);
INSERT INTO Cars (make_model_id, color_id, available) VALUES (1, 2, 0);
INSERT INTO Cars (make_model_id, color_id, available) VALUES (3, 2, 0);

.header on 
SELECT * FROM Colors;
SELECT * FROM MakeModels;
SELECT * FROM Cars;


SELECT Cars.car_id, MakeModels.Make, MakeModels.model, MakeModels.year, Colors.color, Cars.available
FROM Cars
    INNER JOIN MakeModels ON MakeModels.make_model_id = Cars.make_model_id
    INNER JOIN Colors ON Colors.color_id = Cars.color_id;

```

### Updating Values


```
DROP TABLE Colors;
DROP TABLE MakeModels;
DROP TABLE Cars;

CREATE TABLE Colors (
   color_id INTEGER PRIMARY KEY,
   color  TEXT NOT NULL,
   UNIQUE (color)
);

CREATE TABLE MakeModels (
  make_model_id     INTEGER PRIMARY KEY, 
  Make   TEXT NOT NULL,
  Model   TEXT NOT NULL,
  Year INTEGER NOT NULL,
  UNIQUE (Make, Model)
);

CREATE TABLE Cars (
   car_id INTEGER PRIMARY KEY,
   make_model_id INTEGER NOT NULL,
   color_id INTEGER NOT NULL,
   available INTEGER NOT NULL,
   FOREIGN KEY(make_model_id) REFERENCES MakeModels(make_model_id),
   FOREIGN KEY(color_id) REFERENCES Colors(color_id)
);

INSERT INTO Colors (color) VALUES ('Red');
INSERT INTO Colors (color) VALUES ('Blue');
INSERT INTO Colors (color) VALUES ('Greene');

INSERT INTO MakeModels (Make, Model, Year) VALUES ('Frd', 'Explorer', 2019);
INSERT INTO MakeModels (Make, Model, Year) VALUES ('Toyota', 'Camrey', 2010);
INSERT INTO MakeModels (Make, Model, Year) VALUES ('Honda', 'Accord', 2015);

INSERT INTO Cars (make_model_id, color_id, available) VALUES (1, 1, 1);
INSERT INTO Cars (make_model_id, color_id, available) VALUES (2, 1, 1);
INSERT INTO Cars (make_model_id, color_id, available) VALUES (3, 1, 1);
INSERT INTO Cars (make_model_id, color_id, available) VALUES (1, 2, 0);
INSERT INTO Cars (make_model_id, color_id, available) VALUES (1, 2, 0);
INSERT INTO Cars (make_model_id, color_id, available) VALUES (3, 2, 0);
INSERT INTO Cars (make_model_id, color_id, available) VALUES (2, 3, 0);

.header on 
SELECT * FROM Colors;
SELECT * FROM MakeModels;
SELECT * FROM Cars;


SELECT Cars.car_id, MakeModels.Make, MakeModels.Model, MakeModels.year, Colors.color, Cars.available
FROM Cars
    INNER JOIN MakeModels ON MakeModels.make_model_id = Cars.make_model_id
    INNER JOIN Colors ON Colors.color_id = Cars.color_id;

```

```
UPDATE Colors
SET color = 'Green'
WHERE color = "Greene";

SELECT Cars.car_id, MakeModels.Make, MakeModels.Model, MakeModels.year, Colors.color, Cars.available
FROM Cars
    INNER JOIN MakeModels ON MakeModels.make_model_id = Cars.make_model_id
    INNER JOIN Colors ON Colors.color_id = Cars.color_id;


UPDATE MakeModels
SET Make = 'Ford'
WHERE Make = "Frd";

SELECT Cars.car_id, MakeModels.Make, MakeModels.Model, MakeModels.year, Colors.color, Cars.available
FROM Cars
    INNER JOIN MakeModels ON MakeModels.make_model_id = Cars.make_model_id
    INNER JOIN Colors ON Colors.color_id = Cars.color_id;



UPDATE MakeModels
SET Make = 'Camry'
WHERE Model = "Camery";

SELECT Cars.car_id, MakeModels.Make, MakeModels.Model, MakeModels.year, Colors.color, Cars.available
FROM Cars
    INNER JOIN MakeModels ON MakeModels.make_model_id = Cars.make_model_id
    INNER JOIN Colors ON Colors.color_id = Cars.color_id;


UPDATE Cars
SET available = 1
WHERE car_id = 7;

SELECT Cars.car_id, MakeModels.Make, MakeModels.Model, MakeModels.year, Colors.color, Cars.available
FROM Cars
    INNER JOIN MakeModels ON MakeModels.make_model_id = Cars.make_model_id
    INNER JOIN Colors ON Colors.color_id = Cars.color_id;




UPDATE Cars
SET available = 0
WHERE make_model_id = 1;

```



### Deleting Values

```
PRAGMA foreign_keys = ON
DROP TABLE Cars;
DROP TABLE MakeModels;
DROP TABLE Colors;

CREATE TABLE Colors (
   color_id INTEGER PRIMARY KEY,
   color  TEXT NOT NULL,
   UNIQUE (color)
);

CREATE TABLE MakeModels (
  make_model_id     INTEGER PRIMARY KEY, 
  Make   TEXT NOT NULL,
  Model   TEXT NOT NULL,
  Year INTEGER NOT NULL,
  UNIQUE (Make, Model)
);

CREATE TABLE Cars (
   car_id INTEGER PRIMARY KEY,
   make_model_id INTEGER NOT NULL,
   color_id INTEGER NOT NULL,
   available INTEGER NOT NULL,
   FOREIGN KEY(make_model_id) REFERENCES MakeModels(make_model_id),
   FOREIGN KEY(color_id) REFERENCES Colors(color_id)
);

INSERT INTO Colors (color) VALUES ('Red');
INSERT INTO Colors (color) VALUES ('Blue');
INSERT INTO Colors (color) VALUES ('Greene');

INSERT INTO MakeModels (Make, Model, Year) VALUES ('Ford', 'Explorer', 2019);
INSERT INTO MakeModels (Make, Model, Year) VALUES ('Toyota', 'Camry', 2010);
INSERT INTO MakeModels (Make, Model, Year) VALUES ('Honda', 'Accord', 2015);

INSERT INTO Cars (make_model_id, color_id, available) VALUES (1, 1, 1);
INSERT INTO Cars (make_model_id, color_id, available) VALUES (2, 1, 1);
INSERT INTO Cars (make_model_id, color_id, available) VALUES (3, 1, 1);
INSERT INTO Cars (make_model_id, color_id, available) VALUES (1, 2, 0);
INSERT INTO Cars (make_model_id, color_id, available) VALUES (1, 2, 0);
INSERT INTO Cars (make_model_id, color_id, available) VALUES (3, 2, 0);
INSERT INTO Cars (make_model_id, color_id, available) VALUES (2, 3, 0);

.header on 
SELECT * FROM Colors;
SELECT * FROM MakeModels;
SELECT * FROM Cars;


SELECT Cars.car_id, MakeModels.Make, MakeModels.Model, MakeModels.year, Colors.color, Cars.available
FROM Cars
    INNER JOIN MakeModels ON MakeModels.make_model_id = Cars.make_model_id
    INNER JOIN Colors ON Colors.color_id = Cars.color_id;

```

### Simple Delete
```
DELETE FROM Cars
WHERE available = 0;

SELECT Cars.car_id, MakeModels.Make, MakeModels.Model, MakeModels.year, Colors.color, Cars.available
FROM Cars
    INNER JOIN MakeModels ON MakeModels.make_model_id = Cars.make_model_id
    INNER JOIN Colors ON Colors.color_id = Cars.color_id;

```

### Delete from a linked table
```
DELETE FROM Colors
WHERE color = "Red";

SELECT Cars.car_id, MakeModels.Make, MakeModels.Model, MakeModels.year, Colors.color, Cars.available
FROM Cars
    INNER JOIN MakeModels ON MakeModels.make_model_id = Cars.make_model_id
    INNER JOIN Colors ON Colors.color_id = Cars.color_id;


DELETE FROM Colors
WHERE color = "Red";


DELETE FROM Cars
WHERE car_id IN (1,2,3);

SELECT Cars.car_id, MakeModels.Make, MakeModels.Model, MakeModels.year, Colors.color, Cars.available
FROM Cars
    INNER JOIN MakeModels ON MakeModels.make_model_id = Cars.make_model_id
    INNER JOIN Colors ON Colors.color_id = Cars.color_id;


```


### Altering Tables
 - Can easily add columns to tables
 - Can easily rename tables 
 - To change data type, add/remove restriction, or change column name, you have to create a new table and populate it with old data
 - Can drop a column by using select statement and saving the output to another table


```
PRAGMA foreign_keys = ON
DROP TABLE Cars;
DROP TABLE MakeModels;
DROP TABLE Colors;

CREATE TABLE Colors (
   color_id INTEGER PRIMARY KEY,
   color  TEXT NOT NULL,
   UNIQUE (color)
);

CREATE TABLE MakeModels (
  make_model_id     INTEGER PRIMARY KEY, 
  Make   TEXT NOT NULL,
  Model   TEXT NOT NULL,
  Year INTEGER NOT NULL,
  UNIQUE (Make, Model)
);

CREATE TABLE Cars (
   car_id INTEGER PRIMARY KEY,
   make_model_id INTEGER NOT NULL,
   color_id INTEGER NOT NULL,
   available INTEGER NOT NULL,
   FOREIGN KEY(make_model_id) REFERENCES MakeModels(make_model_id),
   FOREIGN KEY(color_id) REFERENCES Colors(color_id)
);

INSERT INTO Colors (color) VALUES ('Red');
INSERT INTO Colors (color) VALUES ('Blue');
INSERT INTO Colors (color) VALUES ('Greene');

INSERT INTO MakeModels (Make, Model, Year) VALUES ('Ford', 'Explorer', 2019);
INSERT INTO MakeModels (Make, Model, Year) VALUES ('Toyota', 'Camry', 2010);
INSERT INTO MakeModels (Make, Model, Year) VALUES ('Honda', 'Accord', 2015);

INSERT INTO Cars (make_model_id, color_id, available) VALUES (1, 1, 1);
INSERT INTO Cars (make_model_id, color_id, available) VALUES (2, 1, 1);
INSERT INTO Cars (make_model_id, color_id, available) VALUES (3, 1, 1);
INSERT INTO Cars (make_model_id, color_id, available) VALUES (1, 2, 0);
INSERT INTO Cars (make_model_id, color_id, available) VALUES (1, 2, 0);
INSERT INTO Cars (make_model_id, color_id, available) VALUES (3, 2, 0);
INSERT INTO Cars (make_model_id, color_id, available) VALUES (2, 3, 0);

.header on 
SELECT * FROM Colors;
SELECT * FROM MakeModels;
SELECT * FROM Cars;


SELECT Cars.car_id, MakeModels.Make, MakeModels.Model, MakeModels.year, Colors.color, Cars.available
FROM Cars
    INNER JOIN MakeModels ON MakeModels.make_model_id = Cars.make_model_id
    INNER JOIN Colors ON Colors.color_id = Cars.color_id;

```




### Backup a single table
.output dump.sql
.dump <table_name>
.output stdout
```


### Backup whole database
```
.output dump.sql
.dump
.output stdout
```





## Foreign Key
- What is a foreign key? In a relational database, you can relate one table to another table. The two
tables can be related if and only if both tables have one column in common. This column has to be declared as a INTEGER data type that cannot be NULL and has the `PRIMARY KEY` constraint -- example: ColumnName INTEGER NOT NULL PRIMARY KEY;
- IMPORTANT: Foreign key constraint is not enabled by default in SQLite

## SQL basic command review
- Data and commands taken from: https://www.guru99.com/sqlite-tutorial.html

### Load data
```
sqlite3 sampledata.db < sampledata.sql
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

SELECT Tests.TestName 'Test Name', avg(Marks.Mark) 'Average' FROM Marks JOIN Tests USING(TestId) GROUP BY Tests.TestId;
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

### WHERE operator with multiple conditions 
```
SELECT * 
FROM Students 
WHERE (StudentId > 5) AND (StudentName LIKE 'N%');


SELECT * 
FROM Students 
WHERE (StudentId > 5) OR (StudentName LIKE 'N%');
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

