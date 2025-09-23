def add(x: int, y:int) -> int:
    return x + y

def main():
    x = 1
    y = 2
    result = add(x, y)
    output_string = f'The output of add({x}, {y}) is {result}.'
    print(output_string)

if __name__=='__main__':
    main()