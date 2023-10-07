import turtle as t
def draw_rectangle(size):
    for i in range(3):
        t.forward(size)
        t.left(120)

def move_forward(size):
    t.penup()
    t.forward(size)
    t.pendown()

size = 90
draw_rectangle(size)
for i in range(2):
    move_forward(2*size)
    draw_rectangle(size)



t.exitonclick()
