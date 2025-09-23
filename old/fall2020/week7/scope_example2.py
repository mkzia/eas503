
def function1(my_list, my_variable):
	print('my_list before change inside function1', my_list)
	print('my_variable before change inside function1', my_variable)
	my_list.append(30)
	my_variable = 10

	print('my_list after change inside function1', my_list)
	print('my_variable after change inside function1', my_variable)


def function2(my_list, my_vairable):
	# https://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list

	my_list = my_list[:]
	my_list.append(90)
	my_variable = 45

	print('my_list after change inside function2', my_list)
	print('my_variable after change inside function2', my_variable)



def function3():
	my_list = [1, 2, 3, 4]
	my_variable = 0def function2(my_list, my_vairable):
	# https://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list

	my_list = my_list[:]
	my_list.append(90)
	my_variable = 45

	print('my_list after change inside function2', my_list)
	print('my_variable after change inside function2', my_variable)

	function1(my_list, my_variable)

	print('my_list after change1 inside function3', my_list)
	print('my_variable after change1 inside function3', my_variable)

	function2(my_list, my_variable)


	print('my_list after change2 inside function3', my_list)
	print('my_variable after change2 inside function3', my_variable)



function3()

