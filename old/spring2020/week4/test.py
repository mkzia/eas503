# 0     space
# 1     ., ?, !
# 2     ABC
# 3     DEF
# 4     GHI
# 5     JKL
# 6     MNO
# 7     PQRS
# 8     TUV
# 9     WXYZ


from pprint import pprint
def convert_message_to_number(message):
    
    keypad = [
        (0, ' ') ,
        (1, '?, !'),
        (2, 'ABC'),
        (3, 'DEF'),
        (4, 'GHI'),
        (5, 'JKL'),
        (6, 'MNO'),
        (7, 'PQRS'),
        (8, 'TUV'),
        (9, 'WXYZ'),
    ]

    keypad_dict = {}
    for number, chars in keypad:
        multiplyby = 1
        for char in chars:
            keypad_dict[char] = str(number)*multiplyby
            multiplyby += 1

    output = ''
    for ele in message:
        output += keypad_dict[ele.upper()]

    return output

print(convert_message_to_number('ABA'))
