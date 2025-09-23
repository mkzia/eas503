# lambda_ex11.py
# sort array by len of names
students = ['john', 'Janette', 'doe']

sort_func = lambda blah: len(blah)

print(sorted(students, key=sort_func))
