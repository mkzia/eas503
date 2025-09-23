class Person:
    def __init__(self, first_name, last_name, email=''):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __repr__(self):
        return f'{self.first_name} {self.last_name} -- {self.email}'

    def get_email(self):
        return self.email

    def get_full_name(self):
        return f'{self.last_name.title()}, {self.first_name.title()}'



class Student(Person):
    PROGRAMS = ['graduate', 'undergraduate']
    MAX_CREDITS = 12

    def __init__(self, first_name, last_name, email, program):
        super().__init__(first_name, last_name, email)
        if program.lower() not in self.PROGRAMS:
            raise ValueError('program can only be "graduate" or "undergraduate"')
        self.program = program
        self.classes = []
        self.enrolled_credits = 0


    def enroll(self, name_of_course):
        if self.enrolled_credits + name_of_course.credits > self.MAX_CREDITS:
            print('Cannot enroll in class because limit reached')
            return 

        if name_of_course not in self.classes:
            self.classes.append(name_of_course)
            self.enrolled_credits += name_of_course.credits
        else:
            print(f'{self.get_full_name()} is already enrolled in {name_of_course} !')

    def print_classes(self):
        classes = ', '.join(['{}({})'.format(obj.course_name, obj.credits) for obj in self.classes])
        print(f'{classes}')

    def print_self(self):
        print(self)

class Course:
    def __init__(self, course_name, credits):
        self.course_name = course_name
        self.credits = credits

    def __repr__(self):
        return f'{self.course_name}'


    def get_course_name(self):
        return self.course_name


s1 = Student('John', 'Doe', 'jdoe@example.com', 'graduate')
print(s1)

eas503 = Course('EAS503', 3)
eas596 = Course('EAS596', 4)
eas666 = Course('EAS666', 12)


s1.enroll(eas503)
s1.enroll(eas596)
s1.print_classes()
print(s1.enrolled_credits)

s1.enroll(eas666)


s1.print_classes()
print(s1.enrolled_credits)
