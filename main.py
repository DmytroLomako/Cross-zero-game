from turtle import *
speed(100)
pensize(5)
list = [0,0,0,
        0,0,0,
        0,0,0]
turn = 1
def cross(x, y):
    # to center
    penup()
    goto(x, y)
    # draw cross
    color('red')
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
    color('black')

def zero():
    color('green')
    penup()
    forward(25)
    left(90)
    forward(8)
    right(90)
    pendown()
    circle(17)
    penup()
    right(90)
    forward(8)
    left(90) 
    left(180)
    forward(25)
    left(180)
    color('black')
    pendown()

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
            forward(50)

draw_field(0, 0)
text = Turtle()
text.penup()
text.goto(-20, 100)
text.color('red')
text.write('Черга ходу крестика', font = ("Arial", 16, "bold"))

draw = False
def check_win():
    global draw
    win = None
    if list[0] != 0 and list[0] == list[1] and list[0] == list[2]:
        win = list[0]
    elif list[3] != 0 and list[3] == list[4] and list[3] == list[5]:
        win = list[3]
    elif list[6] != 0 and list[6] == list[7] and list[6] == list[8]:
        win = list[6]
    elif list[0] != 0 and list[0] == list[3] and list[0] == list[6]:
        win = list[0]
    elif list[1] != 0 and list[1] == list[4] and list[1] == list[7]:
        win = list[1]
    elif list[2] != 0 and list[2] == list[5] and list[2] == list[8]:
        win = list[2]
    elif list[0] != 0 and list[0] == list[4] and list[0] == list[8]:
        win = list[0]
    elif list[2] != 0 and list[2] == list[4] and list[2] == list[6]:
        win = list[2]
    print(list)
    if win == 1:
        text.clear()
        text.color('red')
        text.write('Переміг крестик', font = ("Arial", 20, "bold"))
        draw = True
    elif win == 2:
        text.clear()
        text.color('green')
        text.write('Переміг нолик', font = ("Arial", 20, "bold"))
        draw = True

def click(x, y):
    global turn, draw
    if draw == False:
        if x >= 0 and x <= 50:
            x = 0
        elif x > 50 and x <= 100:
            x = 1
        elif x > 100 and x <= 150:
            x = 2
        else:
            x = None
        if y <= 50 and y >= 0:
            y = 0
        elif y < 0 and y >= -50:
            y = 1
        elif y <-50 and y >= -100:
            y = 2
        else:
            y = None
        if x != None and y != None:
            index = x + y*3
            if list[index] == 0:
                if turn == 1:
                    draw = True
                    list[index] = 1
                    turn = 0
                    text.clear()
                    text.color('green')
                    text.write('Черга ходу нолика', font = ("Arial", 16, "bold"))
                    cross(x * 50 + 25, y * -50 + 25)
                    draw = False
                elif turn == 0:
                    draw = True
                    list[index] = 2
                    penup()
                    goto(x * 50, y * -50)
                    text.clear()
                    text.color('red')
                    text.write('Черга ходу крестика', font = ("Arial", 16, "bold"))
                    turn = 1
                    zero()
                    draw = False
                check_win()
        print(x, y)
onscreenclick(click)

mainloop()