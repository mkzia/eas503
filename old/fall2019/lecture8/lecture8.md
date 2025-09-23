# Lecture 8
- Foreign key
- Joins
- Altering table
- Using SQLite with Python
- SQL Alchemy 

- Ref: https://www.guru99.com/sqlite-tutorial.html -- example data set and commands
- IMPORTANT: Foreign key constraint is not enabled by default in SQLite


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


