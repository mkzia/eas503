class Person:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email


# class Person:
#     def __init__(self, first_name, last_name, email):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email

#     def __repr__(self):
#         return f'{self.first_name} {self.last_name}'


class Person:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __repr__(self):
        return f'{self.first_name} {self.last_name}'

    def get_email(self):
        return self.email

    def get_full_name(self):
        return f'{self.last_name}, {self.first_name}'


# class Student(Person):

#     def __init__(self, first_name, last_name, email, program):
#         super().__init__(first_name, last_name, email)
#         self.program = program

# class Student(Person):
#     PROGRAMS = ['graduate', 'undergraduate']

#     def __init__(self, first_name, last_name, email, program):
#         super().__init__(first_name, last_name, email)
#         if program.lower() not in self.PROGRAMS:
#             raise ValueError('program can only be "graduate" or "undergraduate"')
#         self.program = program.lower()
#         self.classes = []


#     def enroll(self, name_of_course):
#         self.classes.append(name_of_course)

#     def print_classes(self):
#         classes = ', '.join(self.classes)
#         print(f'{classes}')

# s1 = Student('john', 'doe', 'jdoe@example.edu', 'gradUate')
# print(s1)
# s1.enroll('abc')
# s1.enroll('abc')
# s1.enroll('efg')
# s1.enroll('hij')
# s1.print_classes()


# class Student(Person):
#     PROGRAMS = ['graduate', 'undergraduate']

#     def __init__(self, first_name, last_name, email, program):
#         super().__init__(first_name, last_name, email)
#         if program.lower() not in self.PROGRAMS:
#             raise ValueError('program can only be "graduate" or "undergraduate"')
#         self.program = program
#         self.classes = []


#     def enroll(self, name_of_course):
#         if name_of_course not in self.classes:
#             self.classes.append(name_of_course)
#         else:
#             print(f'Already enrolled in {name_of_course} {self.get_full_name()}!')

#     def print_classes(self):
#         classes = ', '.join(self.classes)
#         print(f'{classes}')

#     def print_self(self):
#         print(self)







# s1 = Student('john', 'doe', 'jdoe@example.edu', 'graduate')
# print(s1)
# s1.enroll('abc')
# s1.enroll('abc')
# s1.enroll('efg')
# s1.enroll('hij')
# s1.print_classes()

class Course:
    def __init__(self, course_name, credits):
        self.course_name = course_name
        self.credits = credits

    def __repr__(self):
        return f'{self.course_name}'


    def get_course_name(self):
        return self.course_name



# class Student(Person):
#     PROGRAMS = ['graduate', 'undergraduate']

#     def __init__(self, first_name, last_name, email, program):
#         super().__init__(first_name, last_name, email)
#         if program.lower() not in self.PROGRAMS:
#             raise ValueError('program can only be "graduate" or "undergraduate"')
#         self.program = program
#         self.classes = []


#     def enroll(self, course):
#         if course not in self.classes:
#             self.classes.append(course)
#         else:
#             print(f'Already enrolled in {course}!')

#     def print_classes(self):
#         classes = ', '.join(sorted([i.course_name for i in self.classes]))
#         print(f'{classes}')





c1 = Course('Math', 3)
c2 = Course('Physics', 4)
c3 = Course('Chemistry', 3)
c4 = Course('English', 3)

s1 = Student('john', 'doe', 'jdoe@example.edu', 'graduate')
print(s1)
s1.enroll(c1)
s1.enroll(c2)
s1.enroll(c3)
s1.enroll(c3)
s1.print_classes()


##########

class Student(Person):
    PROGRAMS = ['graduate', 'undergraduate']
    MAX_CREDITS = 9

    def __init__(self, first_name, last_name, email, program):
        super().__init__(first_name, last_name, email)
        if program.lower() not in self.PROGRAMS:
            raise ValueError('program can only be "graduate" or "undergraduate"')
        self.program = program
        self.classes = []
        self.enrolled_credits = 0

    def enroll(self, course):
        if self.enrolled_credits < self.MAX_CREDITS:
            self.classes.append(course)
            self.enrolled_credits += course.credits
        else:
            print('Cannot enroll')
        # if self.get_total_credits() + course.credits > self.MAX_CREDITS:
        #     print(f'You will be over the max credits! Cannot add {course}.')
        #     return

        # if course not in self.classes:
        #     self.classes.append(course)
        # else:
        #     print(f'Already enrolled in {course}!')

    def print_classes(self):
        classes = ', '.join(sorted([i.course_name for i in self.classes]))
        print(f'{classes}')


    # def get_total_credits(self):
    #     total_credits = 0
    #     for ele in self.classes:
    #         total_credits += ele.credits
    #     return total_credits

class Course:
    def __init__(self, course_name, credits):
        self.course_name = course_name
        self.credits = credits

    def __repr__(self):
        return f'{self.course_name}'

    def __str__(self):
        return f'{self.course_name}'


    def get_course_name(self):
        return self.course_name


# c1 = Course('Math', 3)
# c2 = Course('Physics', 4)
# c3 = Course('Chemistry', 3)
# c4 = Course('English', 3)

# s1 = Student('john', 'doe', 'jdoe@example.edu', 'graduate')
# print(s1)
# s1.enroll(c1)
# s1.enroll(c1)
# s1.enroll(c3)
# s1.enroll(c4)
# s1.enroll(c2)
# s1.print_classes()
