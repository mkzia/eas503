# # F = C * 9/5 +32

# celsius = 0
# fahrenheit = celsius * 9/5 + 32
# print(fahrenheit)

# celsius = 100
# fahrenheit = celsius * 9/5 + 32
# print(fahrenheit)


# celsius = 23
# fahrenheit = celsius * 9/5 + 32
# print(fahrenheit)

c_list = [0, 23, 100]

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def c_to_f_and_print(celsius):
    value = celsius_to_fahrenheit(celsius)
    print(value)

for celsius_value in c_list:
    c_to_f_and_print(celsius_value)

# c_to_f_and_print(c_list[0])
# c_to_f_and_print(c_list[1])
# c_to_f_and_print(c_list[2])

# value_0 = celsius_to_fahrenheit(c_list[0])
# print(value_0)

# value_0 = celsius_to_fahrenheit(c_list[1])
# print(value_0)

# value_0 = celsius_to_fahrenheit(c_list[2])
# print(value_0)

# # print(celsius_to_fahrenheit(100)

# def happy():
#     print('Happy birthday to you!')

# def happy_john():
#     print('Happy birthday, dear John!')

# def happy_jane():
#     print('Happy birthday, dear Jane!')

# def happy_name(name):
#     print(f'Happy birthday, dear {name}')

# print('Happy birthday to you!')
# print('Happy birthday to you!')
# print('Happy birthday, dear John!')
# print('Happy birthday to you!')

# print()

# happy()
# happy()
# happy_john()
# happy()

# happy()
# happy()
# happy_jane()
# happy()

# print()



# happy()
# happy()
# happy_name('Wei')
# happy()

# def sing_song(name):
#     happy()
#     happy()
#     happy_name(name)
#     happy()


# print()


# sing_song('Ashish')
