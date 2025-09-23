# lambda_ex4.py
# 1) Write a function to double a list
# 2) Use list comprehension to double a list
# 3) Use lambda with map to double a list

# lambda functions are used with other functions. Usually with map, filter, sort
# map objects are a generator. How many times can you iterate over them?


def double_list(lst):
	output = []
	for ele in lst:
		output.append(ele*ele)

	return output

def double_list2(lst):

	return [ele*ele for ele in lst]

#map(fun, iter)


dlst = lambda x: x*x


print(double_list([1,3,4]))
print(double_list2([1,3,4]))

out = map(dlst, [1,3,4])
print(list(out))