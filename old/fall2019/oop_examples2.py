class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Student(Person):
    def __init__(self, first_name, last_name, credit_hours, q_point):
        super().__init__(first_name, last_name)
        self.credit_hours = credit_hours
        self.q_point = q_point


    def get_gpa(self):
        return round(self.q_point/self.credit_hours, 2)


file_name = input('Enter name of data file: ')

students = []

with open(file_name, 'r') as datafile:
    for line in datafile:
        line = line.strip()
        name, credit_hours, q_point = line.split('\t')
        last_name, first_name = name.split(',')
        temp_variable  = Student(first_name.strip(), last_name.strip(), int(credit_hours), int(q_point))
        students.append(temp_variable)

print(students)
student_best_gpa = students[0]
student_worst_gpa = students[0]
for student in students:
    if student.get_gpa() > student_best_gpa.get_gpa():
        student_best_gpa = student
    if student.get_gpa() < student_worst_gpa.get_gpa():
        student_worst_gpa = student

print('Student with best GPA ', student_best_gpa, student_best_gpa.get_gpa())

print('Student with worst GPA ', student_worst_gpa, student_worst_gpa.get_gpa())

