def input_number(message):
    while True:
        try:
            num = int(input(message))
            return num
        except ValueError:
            print('not valid number, try again')

x = input_number('Enter a number: ')
y = input_number('Enter another number: ')

print(f'x = {x}, y = {y}')
