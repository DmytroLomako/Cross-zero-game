from turtle import *
speed(100)
list = [0,0,1,
        0,0,0,
        2,0,0]
def cross(x, y):
    # to center
    penup()
    goto(x, y)
    # draw cross
    left(45)
    pendown()
    forward(20)
    left(180)
    forward(40)
    penup()
    goto(x, y)
    pendown()
    right(90)
    forward(20)
    right(180)
    forward(40)
    # go to angle
    penup()
    left(45)
    goto(x - 25, y - 25)
    pendown()

def zero():
    forward(25)
    penup()
    left(90)
    forward(5)
    right(90)
    pendown()
    circle(20)
    penup()
    right(90)
    forward(5)
    pendown()
    left(90) 
    left(180)
    forward(25)
    left(180)

def draw_figure(size, count):
    for i in range(count):
        forward(size)
        left(360/count)
def draw_field(x, y):
    penup()
    goto(x, y)
    pendown()
    for i in range(3):
        penup()
        goto(x, y-50*i)
        pendown()
        for j in range(3):
            draw_figure(50, 4)
            index = j + i*3
            if list[index] == 1:
                x_angle = x + 50*j
                y_angle = y - 50*i
                cross(x_angle + 25, y_angle + 25)
            elif list[index] == 2:
                zero()
            forward(50)

draw_field(-50, 50)

# speed(100)
# color("red")
# pensize(5)

# draw_figure(50, 9)

# penup()
# goto(-100, -100)
# pendown()
# forward(50)
# circle(20)
# draw_figure(50, 4)





exitonclick()