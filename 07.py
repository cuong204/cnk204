import turtle as t

while True:

    result = str(input('Nhap yeu cau: '))

    if result in ('triangle', 'square'):
        break
    else:
        print('Invalid, please enter again: ')

length = 100
t.pensize(10)
t.pencolor('pink')

if result == 'triangle':
    t.penup()
    t.goto(-100, -13)
    t.pendown()

    t.forward(length)
    t.left(120)
    t.forward(length)
    t.left(120)
    t.forward(length)
    t.left(120)

    t.done()

else:
    t.penup()
    t.goto(-100, -13)
    t.pendown()

    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)

    t.done


