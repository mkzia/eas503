# define two sets
A = {0, 2, 4, 6, 8};
B = {1, 2, 3, 4, 5};

# 2 in A

# # union -- all values
A | B

# # intersection -- shared values
A & B

# # difference -- order matters
A - B
B - A

# # symmetric difference  https://en.wikipedia.org/wiki/Symmetric_difference
A ^ B


# iteration
for ele in A:
	print(ele)

# Add an element/member to a set
## Add one member
A.add('eight')
A.update(('nine', 'ten'))

my_list = [1, 1, 2, 3]
my_list = list(set(my_list))
A.add('eight')