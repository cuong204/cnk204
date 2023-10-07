while True:

    number1 = int(input("First number: "))
    number2 = int(input("Second number: "))

    if number2 != 0:
        break

    print('You can’t divide by zero, please try again: ')

while True:
    
    op = input("Operation [+, -, *, /]: ")
    if op in ('+', '-', '*', '/'):
        if op == "+":
            result = number1 + number2
            break
        elif op == "-":
            result = number1 - number2
            break
        elif op == "*":
            result = number1 * number2
            break
        else:
            result = number1 / number2
            break
    print('Invalid operation, try again: ')

print(result)

print()
input("Press return to continue ...")