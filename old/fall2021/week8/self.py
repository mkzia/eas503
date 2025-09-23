class TestClass:
    class_variable = 1 # Belongs to the class. Shared by all instances



t1 = TestClass()
t2 = TestClass()


print('\nPrint class_variable')
print('t1.class_variable: ', t1.class_variable)
print('t2.class_variable: ', t2.class_variable)


print('\nChange class_variable in class definition and print class_variable')
TestClass.class_variable = 2
print('t1.class_variable: ', t1.class_variable)
print('t2.class_variable: ', t2.class_variable)


print('\nChange class_variable in instance t1 and print class_variable')
t1.class_variable = 3
print('t1.class_variable: ', t1.class_variable)
print('t2.class_variable: ', t2.class_variable)


print('\nChange class_variable in instance t2 and print class_variable')
t2.class_variable = 4
print('t1.class_variable: ', t1.class_variable)
print('t2.class_variable: ', t2.class_variable)


print('\n', '-'*60, '\n')


class TestClass:
    class_variable = 1 # Belongs to the class. Shared by all instances

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable


t1 = TestClass(1)
t2 = TestClass(2)


print('\nPrint class_variable')
print('t1.class_variable: ', t1.class_variable)
print('t2.class_variable: ', t2.class_variable)

print('\nPrint instance_variable')
print('t1.instance_variable: ', t1.instance_variable)
print('t2.instance_variable: ', t2.instance_variable)


print('\nChange class_variable in class definition and print class_variable')
TestClass.class_variable = 2
print('t1.class_variable: ', t1.class_variable)
print('t1.class_variable: ', t2.class_variable)


print('\nChange instance_variable for t1 and print instance_variable')
t1.instance_variable = 10
print('t1.instance_variable: ', t1.instance_variable)
print('t2.instance_variable: ', t2.instance_variable)

print('\nChange instance_variable for t2 and print instance_variable')
t2.instance_variable = 20
print('t1.instance_variable: ', t1.instance_variable)
print('t2.instance_variable: ', t2.instance_variable)


print('\nChange class_variable in instance t1 and print class_variable')
t1.class_variable = 3
print('t1.class_variable: ', t1.class_variable)
print('t2.class_variable: ', t2.class_variable)


print('\nChange class_variable in instance t2 and print class_variable')
t2.class_variable = 4
print('t1.class_variable: ', t1.class_variable)
print('t2.class_variable: ', t2.class_variable)



print('\n', '-'*60, '\n')


class TestClass:
    class_variable = 1

    # @staticmethod are bound to class rather than object. Therefore, to use them, you do not have
    # to instantiate an object.
    # NOTE: staticmethods do no have access to class properties (variables or methods).
    # This means they cannot access class_variable.
    # Such methods are used when you do not want subclasses to change/overwrite a specific method.

    @staticmethod
    def add(number1, number2):
        return number1 + number2


print('@staticmethod add: ', TestClass.add(3,4))


class TestClass2:
    class_variable = 1

    # @staticmethod are bound to class rather than object. Therefore, to use them, you do not have
    # to instantiate an object.
    # NOTE: staticmethods do no have access to class properties (variables or methods).
    # This means they cannot access class_variable.
    # Such methods are used when you do not want subclasses to change/overwrite a specific method.

    @staticmethod
    def add(number1, number2):
        return number1 + number2# + class_variable

print('@staticmethod add: ', TestClass2.add(3,4))
print('\n', '-'*60, '\n')

class TestClass:
    class_variable = 1

    # @classmethod are bound to class rather than object. Therefore, to use them, you do not have
    # to instantiate an object.
    # NOTE: Unlike staticmethods, classmethods do have access to class properties (variables or methods).
    # This means they can access class_variable.

    @classmethod
    def add(cls, number1, number2):
        return number1 + number2
print('@classmethod add: ', TestClass.add(5,6))



class TestClass2:
    class_variable = 1

    # @classmethod are bound to class rather than object. Therefore, to use them, you do not have
    # to instantiate an object.
    # NOTE: Unlike staticmethods, classmethods do have access to class properties (variables or methods).
    # This means they can access class_variable.

    @classmethod
    def add(cls, number1, number2):
        return number1 + number2 + cls.class_variable

print('@classmethod add -- access to class variable: ', TestClass2.add(5,6))


print('\n', '-'*60, '\n')


class TestClass:
    class_variable = 1

    @staticmethod
    def add_static(number1, number2):
        return number1 + number2

    @classmethod
    def add_class(cls, number1, number2):
        return number1 + number2 + cls.class_variable


    def add_object(self, number1, number2):
        return number1 + number2 + self.class_variable + 29


print('add_static: ', TestClass.add_static(13,14))
print('add_class: ', TestClass.add_class(13,14))


t1 = TestClass()

print('Call from class -- add_object: ', TestClass.add_object(t1, 13, 14))
print('Call from object -- add_object: ', t1.add_object(13, 14))
