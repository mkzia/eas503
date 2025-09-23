CREATE TABLE [Departments] (  
    [DepartmentId] INTEGER  NOT NULL PRIMARY KEY,  
    [DepartmentName] TEXT NULL  
);  
INSERT INTO Departments VALUES(1, 'IT');
INSERT INTO Departments VALUES(2, 'Physics');
INSERT INTO Departments VALUES(3, 'Arts');
INSERT INTO Departments VALUES(4, 'Math');

CREATE TABLE [Students] (  
    [StudentId] INTEGER  PRIMARY KEY NOT NULL,  
    [StudentName] TEXT NOT NULL,  
    [DepartmentId] INTEGER  NULL, 
    [DateOfBirth] DATE NULL,
    FOREIGN KEY(DepartmentId) REFERENCES Departments(DepartmentId)
);  
INSERT INTO Students VALUES(1, 'Michael', 1, '1998-10-12');
INSERT INTO Students VALUES(2, 'John', 1, '1998-10-12');
INSERT INTO Students VALUES(3, 'Jack', 1, '1998-10-12');
INSERT INTO Students VALUES(4, 'Sara', 2, '1998-10-12');
INSERT INTO Students VALUES(5, 'Sally', 2, '1998-10-12');
INSERT INTO Students VALUES(6, 'Jena', NULL, '1998-10-12');
INSERT INTO Students VALUES(7, 'Nancy', 2, '1998-10-12');
INSERT INTO Students VALUES(8, 'Adam', 3, '1998-10-12');
INSERT INTO Students VALUES(9, 'Stevens', 3, '1998-10-12');
INSERT INTO Students VALUES(10, 'George', NULL, '1998-10-12');

CREATE TABLE [Tests] (
    [TestId] INTEGER NOT NULL PRIMARY KEY,
    [TestName] TEXT NOT NULL,
    [TestDate] DATE NULL
);
INSERT INTO [Tests] VALUES(1, 'Mid Term IT Exam', '2015-10-18');
INSERT INTO [Tests] VALUES(2, 'Mid Term Physics Exam', '2015-10-23');
INSERT INTO [Tests] VALUES(3, 'Mid Term Arts Exam', '2015-10-10');
INSERT INTO [Tests] VALUES(4, 'Mid Term Math Exam', '2015-10-15');

CREATE TABLE [Marks] (  
    [MarkId] INTEGER NOT NULL PRIMARY KEY,
    [TestId] INTEGER NOT NULL,
    [StudentId] INTEGER  NOT NULL,  
    [Mark] INTEGER  NULL,
    FOREIGN KEY(StudentId) REFERENCES Students(StudentId),
    FOREIGN KEY(TestId) REFERENCES Tests(TestId) 
);  

INSERT INTO Marks VALUES(1, 1, 1, 18);
INSERT INTO Marks VALUES(2, 1, 2, 20);
INSERT INTO Marks VALUES(3, 1, 3, 16);
INSERT INTO Marks VALUES(4, 2, 4, 19);
INSERT INTO Marks VALUES(5, 2, 5, 14);
INSERT INTO Marks VALUES(6, 2, 7, 20);
INSERT INTO Marks VALUES(7, 3, 8, 20);
INSERT INTO Marks VALUES(8, 3, 9, 20);