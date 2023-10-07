math = int(input('Enter math grade: '))
english = int(input('Enter english grade: '))
physics = int(input('Enter physics grade: '))

if math < 0 or math > 10:
    print('Invalid math grade')
elif english < 0 or english > 10:
    print('Invalid english grade')
elif physics < 0 or physics > 10:
    print('Invalid physic grade')
else:
    avg = (math + english + physics) / 3
    print('Average grade', avg)
    print(math)
    print(english)
    print(physics)
    average = (math + english + physics) / 3
    print(f"The average: {average:.2f}")
    if average < 4:
        print("Failed")
    elif average <= 6.5:
        print("Pass")
    elif average <= 8:
        print("Merit")
    else:
        print("Distinction")



