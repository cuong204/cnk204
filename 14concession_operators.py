name = str(input("Enter your name: "))

age = int(input("Enter your age: "))

student = str(input("Are you a student? [y/n]: "))

if name == 'Chris':
    print('Hello ', name, end='-  - congratulations, you are entitled to a 30% discount')
else:
    if student == 'y' and age <= 18:
        print('Hello ' + name + ' - congratulations, you are entitled to a 20% discount')
    elif student in ('y', 'n') and age > 65:
        print(' - congratulations, you are entitled to a 10% discount')
    else:
        print(' - sorry, you must pay the regular price')

print()
input("Press return to continue ...")