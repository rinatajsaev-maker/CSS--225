#Author:Rinat.R
#Date:11.08.25
#Problem 5:
"""this program draws concentric squares"""

import turtle

def drawSquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("white")

alex = turtle.Turtle()
alex.color("blue")
alex.pensize(2)

size = 20
for i in range(5):
    drawSquare(alex, size)
    alex.penup()
    alex.goto(-10 * (i + 1), -10 * (i + 1))
    alex.pendown()
    size += 20

wn.exitonclick()