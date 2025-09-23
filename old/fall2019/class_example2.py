my_variable = 'Hello, I am variable'

def test():
    global my_variable
    global x
    my_variable = 'I have been changed!'
    x = 10
    print(my_variable)
    can_i_be_accessed = 'whatever'
    print(x)

test()
print(x)


def test2():
    print(x)

test2()

# value = True

# def test3():
#     global value
#     value = False
#     print(value)


# # print(my_variable)
# # test()
# # saved = test2()
# # print(saved)


# print(value)
# test3(value)
# print(value)

# my_list = [1, 2, 3, 4]

# def modify_list(input_list):
#     input_list[2] = 10

# def dontmodify(input_list):
#     import copy
#     copy_list = copy.deepcopy(input_list)
#     copy_list[2] = 10
#     print(copy_list)

# print(my_list)
# dontmodify(my_list)
# print(my_list)

# global x
# x = 2

# def test4(x):
#     x = 5
#     print(x)

# test4(2)
# print(x)

