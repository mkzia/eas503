# lambda_ex6.py
# Using lambda and map, convert the numbers to float


float_lambda = lambda number: float(number)

numbers = ['12', '14', '89']

output = map(float_lambda, numbers)
print(list(output))