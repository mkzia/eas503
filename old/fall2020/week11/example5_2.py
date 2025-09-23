import sqlite3
from sqlite3 import Error



def create_connection(db_file, delete_db=False):
    import os
    if delete_db and os.path.exists(db_file):
        os.remove(db_file)

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


def insert_employee(conn, values):
    sql = """ INSERT INTO EMPLOYEES VALUES(?, ?, ?) """
    cur = conn.cursor()
    cur.execute(sql, values)
    return cur.lastrowid

def insert_project(conn, values):
    sql = """ INSERT INTO PROJECTS VALUES(?, ?) """
    cur = conn.cursor()
    cur.execute(sql, values)
    return cur.lastrowid

def insert_employee_project(conn, values):
    sql = """ INSERT INTO EMPLOYEES_PROJECTS VALUES(?, ?) """
    cur = conn.cursor()
    cur.execute(sql, values)
    return cur.lastrowid


def execute_sql_statement(sql_statement):
    cur = conn.cursor()
    cur.execute(sql_statement)

    rows = cur.fetchall()

    return rows



create_employee_table_sql = """CREATE TABLE [EMPLOYEES] (  
    [EmployeeID] TEXT  NOT NULL PRIMARY KEY,
    [Last_Name] TEXT NOT NULL,
    [First_Name] TEXT NOT NULL
);"""

create_projects_table_sql = """ CREATE TABLE [PROJECTS] (  
    [ProjectNum] TEXT  NOT NULL,
    [ProjectTitle] TEXT NOT NULL,
    PRIMARY KEY (ProjectNum, ProjectTitle)
);
"""

create_employees_projects_table_sql = """ CREATE TABLE [EMPLOYEES_PROJECTS] (  
    [EmployeeID] TEXT  NOT NULL,
    [ProjectNum] TEXT NOT NULL,
    PRIMARY KEY (EmployeeID, ProjectNum)
);
"""


employees = (
    ("EN1-26", "O'Brien", "Sean"),
    ("EN1-33", "Guya", "Amy"),
    ("EN1-35", "Baranco", "Steven"),
    ("EN1-36", "Roslyn", "Elizabeth"),
    ("EN1-38", "Schaaf", "Carol"),
    ("EN1-40", "Wing", "Alexandra")
)

projects = (
    ("30-452-T3", "STAR manual"),
    ("30-457-T3", "ISO procedures"),
    ("30-482-TC", "Web site"),
    ("31-124-T3", "Employee handbook"),
    ("31-238-TC", "STAR prototype"),
    ("31-238-TC2", "New catalog"),
    ("35-152-TC", "STAR pricing"),
    ("36-272-TC", "Order system"),
)


employees_projects = (
    ("EN1-26", "30-452-T3"),
    ("EN1-26", "30-457-T3"),
    ("EN1-26", "31-124-T3"),
    ("EN1-33", "30-328-TC"),
    ("EN1-33", "30-452-T3"),
    ("EN1-33", "32-244-T3"),
    ("EN1-35", "30-452-T3"),
    ("EN1-35", "31-238-TC"),
    ("EN1-36", "35-152-TC"),
    ("EN1-38", "36-272-TC"),
    ("EN1-40", "31-238-TC2"),
    ("EN1-40", "31-241-TC"),
)


db_file = 'example5_py2.db'
conn = create_connection(db_file, True)


with conn:
    create_table(conn, create_employee_table_sql)
    create_table(conn, create_projects_table_sql)
    create_table(conn, create_employees_projects_table_sql)

    for ele in employees:
        insert_employee(conn, ele)
    for ele in projects:
        insert_project(conn, ele)
    for ele in employees_projects:
        insert_employee_project(conn, ele)

    print(execute_sql_statement("SELECT * FROM EMPLOYEES;"))
    print(execute_sql_statement("SELECT * FROM PROJECTS;"))
    print(execute_sql_statement("SELECT * FROM EMPLOYEES_PROJECTS;"))
    print(execute_sql_statement("SELECT EmployeeID, count(ProjectNum) FROM EMPLOYEES_PROJECTS GROUP BY EmployeeID;"))
    sql_statement = """SELECT EMPLOYEES_PROJECTS.EmployeeID, EMPLOYEES_PROJECTS.ProjectNum, EMPLOYEES.Last_Name, EMPLOYEES.First_Name, PROJECTS.ProjectTitle FROM EMPLOYEES_PROJECTS 
LEFT JOIN EMPLOYEES ON EMPLOYEES_PROJECTS.EmployeeID = EMPLOYEES.EmployeeID
LEFT JOIN PROJECTS ON EMPLOYEES_PROJECTS.ProjectNum = PROJECTS.ProjectNum;"""
    for ele in execute_sql_statement(sql_statement):
        print(ele)