import os
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        conn.execute("PRAGMA foreign_keys = 1")
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def insert_depts(conn, values):
    sql = ''' INSERT INTO Departments(DepartmentName)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, values)
    return cur.lastrowid


def insert_student(conn, values):
    sql = ''' INSERT INTO Students(StudentName, DepartmentId, DateOfBirth)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, values)
    return cur.lastrowid


def select_all_students(conn):
    cur = conn.cursor()
    cur.execute("""SELECT * FROM Students INNER JOIN Departments USING(DepartmentId);""")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    return rows


db_file = 'sample_data_py.db'
if os.path.exists(db_file):
    os.remove(db_file)

create_table_departments_sql = """ CREATE TABLE [Departments] (
    [DepartmentId] INTEGER  NOT NULL PRIMARY KEY,
    [DepartmentName] NVARCHAR(50)  NULL
); """

create_table_students_sql = """ CREATE TABLE [Students] (
    [StudentId] INTEGER  PRIMARY KEY NOT NULL,
    [StudentName] NVARCHAR(50) NOT NULL,
    [DepartmentId] INTEGER  NULL,
    [DateOfBirth] DATE NULL,
    FOREIGN KEY(DepartmentId) REFERENCES Departments(DepartmentId)
);  """

conn = create_connection(db_file)


depts = ('IT', 'Physics', 'Arts', 'Math')
students = (
    ('Michael', 1, '1998-10-12'),
    ('John', 1, '1998-10-12'),
    ('Jack', 1, '1998-10-12'),
    ('Sara', 2, '1998-10-12'),
    ('Sally', 2, '1998-10-12'),
    ('Jena', None, '1998-10-12'),
    ('Nancy', 2, '1998-10-12'),
    ('Adam', 3, '1998-10-12'),
    ('Stevens', 3, '1998-10-12'),
    ('George', None, '1998-10-12')
)

with conn:

    create_table(conn, create_table_departments_sql)
    create_table(conn, create_table_students_sql)
    for values in depts:
        insert_depts(conn, (values, ))
    for values in students:
        insert_student(conn, values)
    select_all_students(conn)


conn = create_connection(db_file)
import pandas as pd
sql_statement = "select * from students;"
df = pd.read_sql_query(sql_statement, conn)
print(df)