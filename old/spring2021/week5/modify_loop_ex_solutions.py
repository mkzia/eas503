# Ex1
# Write a function that prints from 1 to n using a for loop, it should skip every
# multiple of 5

def modify_loop_ex1(n):
    for number in range(n):

        if number % 5 == 0:
            print('Skipping:', number)
            continue

        print(number)


# Ex2
# Write a function that prints from 1 to n squared using a while loop.
# It should stop the while loop if the iteration count is 50. 


def modify_loop_ex2(n):

    iteration_count = 0
    number = 1
    while number <= n:

        if number == 50:
            break

        print(number)
        number += 1
        iteration_count += 1



# Ex3
# Write a function that reads numbers from a file and prints their average. 
# Skip empty lines
def modify_loop_ex3(filename):

    numbers = []
    with open(filename) as file:
        for line in file:
            if not line.strip():
                continue

            numbers.append(float(line))

    print(round(sum(numbers)/len(numbers),2))




modify_loop_ex1(40)

modify_loop_ex2(100)

modify_loop_ex3('modify_loop_ex3_data.txt')