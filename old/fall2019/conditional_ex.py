
# celsius = float(input("What is the Celsius temperature? "))
# fahrenheit = 9/5 * celsius + 32
# print("The temperature is", fahrenheit, "degrees fahrenheit.")




# Lets add a print statement if temperature in F > 90 or F < 32

# def our_function():
#     celsius = float(input("What is the Celsius temperature? "))
#     fahrenheit = 9/5 * celsius + 32
#     print("The temperature is", fahrenheit, "degrees fahrenheit.")

#     if fahrenheit > 95: # <expr> <relop> <expr>, where <relop> is relation operator
#         print("It's really hot out there. Be careful!")

#     if fahrenheit < 32: # <expr> <relop> <expr>, where <relop> is relation is operator
#         print("Be sure to dress warmly!")

# our_function()

# # If this, otherwise that -- If Else conditional
# import math
# print("This program finds the real solutions to a quadratic\n")
# a = float(input("Enter coefficient a: "))
# b = float(input("Enter coefficient b: "))
# c = float(input("Enter coefficient c: "))
# disc_root = math.sqrt(b * b -4 * a * c)

# root1 = (-b + disc_root) / (2 * a)
# root2 = (-b - disc_root) / (2 * a)

# print("\nThe solutions are:", root1, root2)


# If this, otherwise that -- If Else conditional
# import math
# print("This program finds the real solutions to a quadratic\n")
# a = float(input("Enter coefficient a: "))
# b = float(input("Enter coefficient b: "))
# c = float(input("Enter coefficient c: "))
# discrim = b * b -4 * a * c

# if discrim < 0:
#     print("\nThe equation has no real roots!")
# else:
#     disc_root = math.sqrt(b * b - 4 * a * c)
#     root1 = (-b + disc_root) / (2 * a)
#     root2 = (-b - disc_root) / (2 * a)
#     print("\nThe solutions are:", root1, root2)

# If this, otherwise that -- If Else conditional
# import math
# print("This program finds the real solutions to a quadratic\n")
# a = float(input("Enter coefficient a: "))
# b = float(input("Enter coefficient b: "))
# c = float(input("Enter coefficient c: "))
# discrim = b * b -4 * a * c

# if discrim < 0:
#     print("\nThe equation has no real roots!")
# else:
#     if discrim == 0:
#         root = -b / (2 * a)
#         print("\nThere is a double root at:", root)
#     else:
#         disc_root = math.sqrt(b * b - 4 * a * c)
#         root1 = (-b + disc_root) / (2 * a)
#         root2 = (-b - disc_root) / (2 * a)
#         print("\nThe solutions are:", root1, root2)



# # # If this, otherwise that -- If Else conditional
import math
# print("This program finds the real solutions to a quadratic\n")
# a = float(input("Enter coefficient a: "))
# b = float(input("Enter coefficient b: "))
# c = float(input("Enter coefficient c: "))
# discrim = b * b -4 * a * c

# if discrim < 0:
#     print("\nThe equation has no real roots!")
# elif discrim == 0:
#     root = -b / (2 * a)
#     print("\nThere is a double root at:", root)
# else:
#     disc_root = math.sqrt(b * b - 4 * a * c)
#     root1 = (-b + disc_root) / (2 * a)
#     root2 = (-b - disc_root) / (2 * a)
#     print("\nThe solutions are:", root1, root2)

# x1 = 25
# x2 = 10
# x3 = 45

# if x1 >= x2 and x1 >= x3:
#     maxval = x1
# elif x2 >= x1 and x2 >= x3:
#     maxval = x2
# else:
#     maxval = x3

# print(maxval)

# import math
# print ("This program finds the real solutions to a quadratic\n")

# try:
#     a = float(input("Enter coefficient a: "))
#     b = float(input("Enter coefficient b: "))
#     c = float(input("Enter coefficient c: "))
#     discRoot = math.sqrt(b * b - 4 * a * c)
#     root1 = (-b + discRoot) / (2 * a)
#     root2 = (-b - discRoot) / (2 * a)
#     print("\nThe solutions are:", root1, root2)
# except ValueError:
#     print("\nNo real roots")


# x = [1, 2, '3', 'three',  7.0]

# new_list = []

# for ele in x:
#     try:
#         new_list.append(float(ele))
#     except ValueError:
#         new_list.append(None)
#      except IndexError:
#         new_list.append(None)

# print(new_list)

# for value in new_list:
#     if value:
#         print(value*value)

# print("This program finds the real solutions to a quadratic\n")

import math
try:
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    discRoot = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)
    print("\nThe solutions are:", root1, root2 )
except ValueError as excObj:
    if str(excObj) == "math domain error":
        print("No Real Roots")
    else:
        print("Invalid coefficient given.")
except IndexError as excObj:
    pass
except:
    print("\nSomething went wrong, sorry!")

my_list = [1, 2, 3]
x = 0
try:
    print(my_list[1].abc())
except ZeroDivisionError as error:
    print(error)
except IndexError as error:
    print(error)
except:
    print('Uncaught error!')
