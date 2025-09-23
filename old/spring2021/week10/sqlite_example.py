# REF: https://www.sqlitetutorial.net/sqlite-python/
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn



def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def insert_student(conn, values):

    sql = ''' INSERT INTO students(last_name,first_name,username,exam1,exam2,exam3)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, values)
    return cur.lastrowid


def select_all_students(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    return rows


import os, pprint


db_file = 'student_test_in_class.db'
if os.path.exists(db_file):
    os.remove(db_file)

create_table_sql = """CREATE TABLE students (last_name TEXT, first_name TEXT, username TEXT, exam1 REAL, exam2 REAL, exam3 REAL);"""

conn = create_connection(db_file)

with conn:
    # create
    # create_table(conn, create_table_sql)

    # # insert
    # for student in open('students.tsv', 'r'):
    #     values = student.strip().split('\t')
    #     rid = insert_student(conn, values)

    # # select
    # rows = select_all_students(conn)

# calculate average of all students
from statistics import mean
student_grades = []
for student in rows:
    username, last_name, first_name, e1, e2, e3 = student
    student_grades.append((username, last_name, first_name, round(mean((e1, e2, e3)),2)))



sorted_grades = sorted(student_grades, key=lambda x: x[-1], reverse=True)
pprint.pprint(sorted_grades)







