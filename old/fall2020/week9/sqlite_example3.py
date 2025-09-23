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

def insert_student2(conn, table, values):
    sql = ''' INSERT INTO ?
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, values)
    return cur.lastrowid


def get_dept_fk(dept):
    cur = conn.cursor()
    cur.execute("""SELECT DepartmentId FROM Departments WHERE DepartmentName == (?);""",  (dept, ))

    fk = cur.fetchone()
    if fk:
        return fk[0]
    else:
        return None


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
    ('Michael', 'IT', '1998-10-12'),
    ('John', 'IT', '1998-10-12'),
    ('Jack', 'IT', '1998-10-12'),
    ('Sara', 'Physics', '1998-10-12'),
    ('Sally', 'Physics', '1998-10-12'),
    ('Jena', None, '1998-10-12'),
    ('Nancy', 'Physics', '1998-10-12'),
    ('Adam', 'Arts', '1998-10-12'),
    ('Stevens', 'Arts', '1998-10-12'),
    ('George', None, '1998-10-12')
)

with conn:

    create_table(conn, create_table_departments_sql)
    create_table(conn, create_table_students_sql)
    for values in depts:
        insert_depts(conn, (values, ))
    for values in students:
        values = list(values)
        print(values)
        values[1] = get_dept_fk(values[1])
        print(values)
        insert_student(conn, values)
    select_all_students(conn)
