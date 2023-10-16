import turtle
import random
turtle.shape("turtle")
scr = turtle.Screen()
scr.bgcolor("black")
turtle.color("white", "red")
turtle.speed(50)
colors = ['white','blue','red','yellow','lightgreen','pink','lightyellow','cyan','skyblue']
def one(y):
    turtle.left(90)
    turtle.forward(y)
    turtle.right(180)
    turtle.forward(y)
    turtle.left(90)
def space(x):
    turtle.penup()
    turtle.forward(x)
    turtle.pendown()
def two(x, y):
    turtle.forward(x)
    turtle.right(180)
    turtle.forward(x)
    turtle.right(90)
    turtle.forward(y)
    turtle.right(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(y)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.penup()
    turtle.forward(y*2)
    turtle.left(90)
    turtle.forward(x)
def three(x, y):
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(y)
    turtle.left(90)
    turtle.forward(y)
    turtle.left(180)
    turtle.forward(y)
    turtle.left(90)
    turtle.forward(y)
    turtle.left(90)
    turtle.forward(x)
def octa(x):
    for i in range(8):
        turtle.color(random.choice(colors))
        turtle.forward(x)
        turtle.left(45)
def rand():
    turtle.forward(random.randint(0, 300))
    turtle.left(random.randint(0, 360))
'''
Q1
turtle.begin_fill
for i in range(4):
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()

Q2
turtle.begin_fill
for i in range(3):
    turtle.forward(100)
    turtle.right(120)
turtle.end_fill()

Q3
turtle.circle(40, 360)

Q4
for i in (1, 2 ,3):
    turtle.begin_fill()
    if i == 2:
        turtle.color("white", "blue")
    elif i == 3:
        turtle.color("white", "green")
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(150)
    turtle.pendown()

Q5
turtle.left(324)
for i in range(5):
    turtle.forward(100)
    turtle.right(216)
    turtle.forward(100)

Q6
one(100)
space(100)
two(100, 50)
space(100)
three(100, 50)

Q7
octa(100)

Q8
for i in range(12):
    octa(100)
    turtle.left(30)

Q9
for i in range(12):
    rand()
'''