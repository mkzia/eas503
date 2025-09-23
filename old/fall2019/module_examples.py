# Modules are used to write functions and classes in a class and save them in a file
# and then import the functions and classes from the file. 

import my_funcs_classes

print(my_funcs_classes.add(1,2))


from my_funcs_classes import add

print(add(3,42))
