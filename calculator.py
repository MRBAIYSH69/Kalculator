x = float(input('Введите первое число: ') )
y = float(input('Введите второе число: ') )
operation = input('Operation: ')
result = None
if operation == '+':
    result = x + y
elif operation == '-':
    result = x - y
elif operation == '*':
    result = x * y
elif operation == '/':
    result = x / y
else:4
    print("Error")

if result is not None:
    print('Result', result )