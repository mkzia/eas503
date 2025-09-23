def PowX(limit, power):
    value = 0
    while value < limit:
        yield value**power
        value += 1

a = PowX(10, 3)

for ele in a:
    print(ele)

for ele in a:
    print(1,ele)
