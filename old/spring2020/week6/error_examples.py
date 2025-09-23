# # SyntaxError -- invalid Python syntax
# def func(()):
#    pass

# for index in some_list
#     print(index)


# # NameError -- using a variable before it has been defined

# def func():
#    print(variable)


# # TypeError -- mismatch data type

# '3' + 3

# # IndexError
# my_list = [1, 2, 3]
# my_list[4]

# # ValueError calling a built-in function with invalid value type

# int('3')
# int('3a')

# # KeyError -- like by index error for lists

# student = {'username': 'john', 'grade': 50}

# student['class']

# # AttributeError -- missing attribute -- variables or methods

# class TestClass:
#     class_variable1 = 2


# print(TestClass.class_variable1)
# print(TestClass.class_variable2)

# string = 'test1234'
# string.upper()

# x = [1,2,3]
# x.upper()

# # More @ https://docs.python.org/3/library/exceptions.html


# # Raising error -- with a message or without message

# raise ValueError('a message')
# raise ValueError


def calculate_bmi(height, weight):

    if type(height) not in [float, int]:
        raise TypeError('Height has to be float or an int')

    if type(weight) not in [float, int]:
        raise TypeError('Weight has to be float or an int')


    if height <= 0:
        raise ValueError('Height cannot be less than or equal to 0')

    if weight <= 0:
        raise ValueError('Weight cannot be less than or equal to 0')

    return 703 * weight / height**2


while True:
    try:
        height = float(input('Please enter height: '))
        weight = float(input('Please enter weight: '))
    except Exception as error:
        print(error)
        print('Please enter a number')
    else:
        print('I run when there is no error')
        break
    finally:
        print('I always run!')

print(calculate_bmi(height, weight))


# Try and Except blocks -- a way to handle errors
# When you raise an error, your program exits. What
# you rather want to do is to catch that error and give
# user feedback.



student = {'username': 'john', 'grade': 50}


def get_key(some_dict, key, default_value=None):
    try:
        return some_dict[key]
    except KeyError:
        return default_value


print(get_key(student, 'username1', default_value='Error'))
print(get_key(student, 'username1'))


# try, except, else, finally


