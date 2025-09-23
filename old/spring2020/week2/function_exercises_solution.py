# 1 ----------------------------
print('_'*40)
print('Happy birthday to you!!!')
print('Happy birthday to you!!!')
print('Happy birthday, dear John')
print('Happy birthday to you!')
print('Happy birthday to you!')
print('_'*40)

# 2 ---------------------------------
print('_'*40)
print('Happy birthday to you!')
print('Happy birthday to you!')
print('Happy birthday, dear Jane')
print('Happy birthday to you!')
print('Happy birthday to you!')
print('_'*40)


# 3 ------------------------------
def print_happy_birthday():
    print('Happy birthday to you!!!')
    print('Happy birthday to you!!!')


# 4a ----------------
print_happy_birthday()
print('Happy birthday, dear John')
print_happy_birthday()

# 4b ----------------
print_happy_birthday()
print('Happy birthday, dear Jane')
print_happy_birthday()


# 5 ----------------------------------
def print_happy_birthday_name(name):
    print(f'Happy birthday, dear {name}')

# 6---------------------------
print_happy_birthday()
print_happy_birthday_name('John')
print_happy_birthday()

print('-'*80)

print_happy_birthday()
print_happy_birthday_name('Jane')
print_happy_birthday()


# 7 ------------------------------------
def calculate_distance(x1,y1,x2,y2):
    import math
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    return distance

# 8 ---------------------------
def coin_toss()
    import random

    number = random.randint(0, 1)

    if number == 0:
        return 'Head'
    else:
        return 'Tail'