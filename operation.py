number1 = int(input('Enter first number:'))
number2 = int(input('Enrer second number: '))

operation = input('choose math operation (+, -, *, / ): ')

if operation !='+' and operation != '-' and operation != '*' and operation != '/' :
    print('Invalid operation')
else:
    if operation == '+':
        result = number1 + number2
    elif operation == '-':
        result = number1 - number2
    elif operation == '*':
        result = number1 * number2
    elif operation == '/':
        result = number1 // number2

print('Result:', result)
