def add_interest(balance, rate):
	new_balance = balance * (1 + rate)
	balance = new_balance

def add_interest2(balance, rate):
	new_balance = balance * (1 + rate)
	balance = new_balance

	return balance

def test():
	amount = 1000
	rate = 0.05
	add_interest(amount, rate)
	print(amount)

def test2():
	amount = 1000
	rate = 0.05
	amount = add_interest2(amount, rate)
	print(amount)


test()
test2()