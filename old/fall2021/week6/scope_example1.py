
variable = 'Global reporting!'


def use_variable_global():
    ## since variable is outside the function
    print(variable)


def use_variable_local():
    variable = 'Local reporting!'
    print(variable)

# def use_variable_global():

def change_global_inside_function():
    global variable
    variable = 'I have been changed!'
    print(variable)


print(variable)
use_variable_global()
use_variable_local()
change_global_inside_function()
print(variable)
