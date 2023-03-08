import turtle as t


t.bgcolor("darkblue")


t.speed(0)
t.bgcolor("lightblue")

#bottom circle
t.color("white")
t.penup()
t.goto(0,-200)
t.pendown()
t.begin_fill()
t.circle(50)
t.end_fill()

t.color("black")
t.penup()
t.goto(0, -200)
t.pendown()
t.circle(50)
t.color("white")
#middle circle
t.penup()
t.goto(0,-115)
t.pendown()
t.begin_fill()
t.circle(35)
t.end_fill()

t.color("black")
t.circle(35)
t.color("white")
#top circle
t.penup()
t.goto(0,-50)
t.pendown()
t.begin_fill()
t.circle(25)
t.end_fill()

t.color("black")
t.circle(25)
t.color("white")
#eyes

t.penup()
t.goto(-7,-15)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(2)
t.end_fill()

t.penup()
t.goto(7, -15)
t.pendown()
t.begin_fill()
t.circle(2)
t.end_fill()

#nose

t.penup()
t.goto(7,-25)
t.left(90)
t.color("orange")
t.pendown()
t.begin_fill()
t.circle(5, 365, 3)
t.end_fill()

#mouth
t.penup()
t.goto(-12, -34)
t.color("black")
t.pendown()
t.begin_fill()
t.circle(2)
t.end_fill()

t.penup()
t.goto(-8, -37)
t.pendown()
t.begin_fill()
t.circle(2)
t.end_fill()

t.penup()
t.goto(-4, -38)
t.pendown()
t.begin_fill()
t.circle(2)
t.end_fill()

#buttons
t.color("saddlebrown")
t.penup()
t.goto(3, -65)
t.pendown()
t.begin_fill()
t.circle(3)
t.end_fill()

t.penup()
t.goto(3, -75)
t.pendown()
t.begin_fill()
t.circle(3)
t.end_fill()

t.penup()
t.goto(3, -85)
t.pendown()
t.begin_fill()
t.circle(3)
t.end_fill()

t.penup()
t.goto(3, -130)
t.pendown()
t.begin_fill()
t.circle(3)
t.end_fill()

t.penup()
t.goto(3, -150)
t.pendown()
t.begin_fill()
t.circle(3)
t.end_fill()

t.penup()
t.goto(3, -170)
t.pendown()
t.begin_fill()
t.circle(3)
t.end_fill()

#hat
t.penup()
t.goto(0,0)
t.color("yellow")
t.pendown()
t.begin_fill()
t.circle(20, 360, 3)
t.end_fill()

t.color("blue")
t.pendown()
t.circle(20, 360, 3)

#arms
t.pensize(3)
t.color("brown")
t.penup()
t.goto(30, -80)
t.seth(75)
t.pendown()
t.fd(90)

t.left(40)
t.pensize(3)
t.fd(10)

t.backward(10)
t.right(40)
t.fd(10)
t.backward(10)

t.right(40)
t.fd(10)

t.penup()
t.goto(-30, -80)
t.seth(115)
t.pendown()
t.fd(90)

t.left(40)
t.pensize(3)
t.fd(10)

t.backward(10)
t.right(40)
t.fd(10)
t.backward(10)

t.right(40)
t.fd(10)

t.penup()
t.goto(0,200)


def draw_flake():
    t.color("white")
    t.pendown()
    for i in range(8):   
        t.fd(20)
        t.backward(5)
        t.left(60)
        t.fd(5)
        t.backward(5)
        t.right(120)
        t.fd(5)
        t.backward(5)
        t.left(60)
        t.backward(15)
        t.left(45)
    t.penup()
t.goto(0, 100)
draw_flake()
t.goto(-100, 50)
draw_flake()
t.goto(-150, 150)
draw_flake()
t.goto(-100, -100)
draw_flake()
t.goto(150, 180)
draw_flake()
