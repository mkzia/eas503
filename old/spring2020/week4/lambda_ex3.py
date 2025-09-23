# lambda_ex3.py
# Write a lambda function that multiples two numbers. 
# Use the lambda function as an input to another function. 

abcd = lambda x,y: x * y

def my_mul(x,y, mul):

	return mul(x,y)


print(my_mul(10,20, abcd))

