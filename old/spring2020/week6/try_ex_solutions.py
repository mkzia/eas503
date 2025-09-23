# Ex1
# Write a function that asks the user to input a number in Celsius and converts to Fahrenheit
# Use Try/Except block to detect non integer

def ex1():
    while True:
        temperature = input('Please enter temperature in Celsius: ')
        try: 
            temperature = float(temperature)
            break
        except Exception as e:
            print(e)
            continue

    print('Temperature in Fahrenheit:', temperature * 1.8 + 32)



ex1()


# Ex2
# Write a function that prompts users to input numbers to calculate their average. Use the word STOP
# to stop input process. 
# Use try and except to discard non-number inputs. 

def ex2():

    numbers = []
    while True:
        number = input('Please enter number to average: ')

        if number == 'STOP':
            break

        try: 
            number = float(number)
        except Exception as e:
            print(e)
            continue

        numbers.append(number)

    print('average:', sum(numbers)/len(numbers))


ex2()
