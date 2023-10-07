age = int(input('tuoi cua ban: '))
if age < 18:
    print('You are not eligible to apply for a driver license')
else:
    if age > 21:
        print('You are eligible to apply for a driver license.')
        print('You are also eligible to rent a car')
    else:
        print('You are eligible to apply for a driver license.')
        print('You need to be at least 21 years old to rent a car')