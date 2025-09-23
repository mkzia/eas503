# Create a Person class with first name and last name
# Create a Student class that inherits from person name 
# and adds credit_hours and q_point
# The Person class should define __repr__ function
# The student class must define get_gpa()
# Read from data.tsv each line and create a student object and
# store it in a list 

#o do the same using in and max



class Person: 

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    def __repr__(self):
        return '{}, {}'.format(self.last_name, self.first_name)


class Student(Person):
    def __init__(self, first_name, last_name, credit_hours, q_point):
        super().__init__(first_name, last_name)
        self.credit_hours = credit_hours
        self.q_point = q_point

    def get_gpa(self):
        return self.q_point/self.credit_hours


students = []
with open('data.tsv') as file:
    for line in file:
        if not line.strip():
            continue

        name, credit_hours, q_point = line.strip().split('\t')
        last_name, first_name = name.split(',')

        s = Student(first_name, last_name, int(credit_hours), int(q_point))
        students.append(s)



max_student = students[0]
min_student = students[0]

for student in students:
    if student.get_gpa() > max_student.get_gpa():
        max_student = student

    if student.get_gpa() < min_student.get_gpa():
        min_student = student

print(max_student, max_student.get_gpa())
print(min_student, min_student.get_gpa())


l_func = lambda student: student.get_gpa()
print(min(students, key=l_func))
print(max(students, key=l_func))
