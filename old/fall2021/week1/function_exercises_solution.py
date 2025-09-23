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

# 8 ----------------------------
def triple(num):
    return num * 3


# 9 -----------------------------
def km_to_miles(km):
    return km / 1.6


# 10 --------------------------
def average_grade(grade1, grade2, grade3):
    return (grade1 + grade2 + grade3) / 3


# 11 -------------------------------
def top_three_avg(grade1, grade2, grade3, grade4):
    total = grade1 + grade2 + grade3 + grade4
    top_three = total -min(grade1, grade2, grade3, grade4)
    return top_three / 3

# 12 -----------------------------------
def weeks_elapsed(day1, day2):
    return int(abs(day1 -day2) / 7)