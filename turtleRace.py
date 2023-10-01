import random
import turtle
turtle.screensize(1000, 1000)
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t1.penup()
t1.goto(0, 100)
t1.pendown()
t2.penup()
t2.goto(0,-100)
t2.pendown()
for i in range(101):
    t1.forward(random.randint(2, 5))
    t2.forward(random.randint(2, 5))
if t1.xcor() >= 200:
    t1.write('Turtle 1 wins!', font=('Arial', 16, 'normal'))
elif t2.xcor() >= 200:
    t2.write('Turtle 2 wins!', font=('Arial', 16, 'normal'))
turtle.done()

print('Hello World')