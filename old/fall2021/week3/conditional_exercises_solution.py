# 1 ---------------------
# Write a program to prompt the user for temperature in Celsius, convert 
# the temperature to Fahrenheit, and print temperature in Fahrenheit. 

celsius = float(input("What is the Celsius temperature? "))
fahrenheit = 9/5 * celsius + 32
print("The temperature is", fahrenheit, "degrees Fahrenheit.")


# 2 ---------------------
# Modify exercise 1 to print a message when F > 90 and F < 32

celsius = float(input("What is the Celsius temperature? "))
fahrenheit = 9/5 * celsius + 32
print("The temperature is", fahrenheit, "degrees Fahrenheit.")

if fahrenheit > 95: # <expr> <relop> <expr>, where <relop> is relation operator
    print("It's really hot out there. Be careful!")

if fahrenheit < 32: # <expr> <relop> <expr>, where <relop> is relation is operator
    print("Be sure to dress warmly!")

# 3 ---------------------
# Write a function to calculate the solution to a quadratic equation
# https://www.mathsisfun.com/algebra/quadratic-equation.html
# Prompt the user to the coefficients a, b, and c. 


import math
print("This program finds the real solutions to a quadratic\n")
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
disc_root = math.sqrt(b * b -4 * a * c)

root1 = (-b + disc_root) / (2 * a)
root2 = (-b - disc_root) / (2 * a)

print("\nThe solutions are:", root1, root2)



# 4 --------------------
# Modify ex3 to add conditionals to print no real roots, double root, roots

# If this, otherwise that -- If Else conditional
import math
print("This program finds the real solutions to a quadratic\n")
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
discrim = b * b -4 * a * c

if discrim < 0:
    print("\nThe equation has no real roots!")
else:
    if discrim == 0:
        root = -b / (2 * a)
        print("\nThere is a double root at:", root)
    else:
        disc_root = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + disc_root) / (2 * a)
        root2 = (-b - disc_root) / (2 * a)
        print("\nThe solutions are:", root1, root2)


# 5 --------------------


# Find the maxval

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
z = int(input("Enter enter a third number: "))

if x1 >= x2 and x1 >= x3:
    maxval = x1
elif x2 >= x1 and x2 >= x3:
    maxval = x2
else:
    maxval = x3

print(maxval)


# 6 ------------------
# Write a program to prompt the user for their user name. 
# If it is jdoe, print a log in allowed message; otherwise, print another message

username = 'jdoe'

if username == 'jdoe':
    print('Hi, John.')
else:
    print('Hello, stranger.')



# 7 -------------------
# Modify ex6 to only allow login if the user is active

active_status = False
username = 'jdoe'

if username =='jdoe' and active_status:
	print('Hi, Jone your are allowed to log in!')
else:
	print('You are not allowed to log in!')

active_status = True
username = 'jdoe'

if username =='jdoe' and active_status:
	print('Hi, Jone your are allowed to log in!')
else:
	print('You are not allowed to log in!')

# 8 -----------------
# Write a program to prompt the user for name and check if it is john or jane

name = input('What is your name? ')
if name == 'john':
	print('Your name is John!')
elif name == 'jane':
	print('Your name is Jane!')


name = input('What is your name? ')
if name == 'john'.lower():
	print('Your name is John!')
elif name == 'jane'.lower():
	print('Your name is Jane!')


# 9 ------------------
# Write a program that only allows a user to log in if they are a superuser or if they are are teach and active

is_super_user = True
is_teacher = True
is_active = False

if is_super_user or (is_teacher and is_active):
	print('You can access the system')


# 10 -----------------
# Prompt user for age and check if they are 18 or older
age = int(input('What is your age? '))

if age >= 18:
	print('You are older 18 or older')
else:
	print('You are not 18!')

# 11 ---------------
# Prompt the user for two numbers and see if they are equal

number1 = int(input('Please enter a number: '))
number2 = int(input('Please enter a number: '))

if number1 == number2:
	print('Both numbers are equal')


# 12 ---------------
# Check if a number is even or odd
number = int(input('Please enter a number: '))

if number == 0:
	print('The number is even')
elif number % 2 == 0:
	print('The number is even')
else: 
	print('The number is odd')
