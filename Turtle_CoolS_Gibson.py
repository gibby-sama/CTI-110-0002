# Google search "Cool S" for reference
# This code will run turtle to draw the "cool S"

# Import turtle & select BG

import turtle

# Assignments
# Vertical lines | Left lines | Right lines | Head lines | Butt lines
# Left/Right Lines are the diagonal lines that connect the vertical lines
# They are coordinated by the direction they're headed towards
# Head/Butt Lines are the diagonal lines at the top & bottom of the S

v = turtle.Turtle()
v.speed(speed=1)
l = turtle.Turtle()
l.speed(speed=1)
r = turtle.Turtle()
h = turtle.Turtle()
b = turtle.Turtle()

## Vertical Lines Code (Variable "v")

# V-Line Upper Left
v.penup()
v.goto(-50, 0)
v.pendown()
v.left(90)
v.forward(50)

#V-Line Upper Middle
v.penup()
v.goto(0, 0)
v.pendown()
v.forward(50)

#V-Line Upper Right
v.penup()
v.goto(50, 0)
v.pendown()
v.forward(50)

#V-Line Lower Left
v.penup()
v.goto(-50, -50)
v.pendown()
v.right(180)
v.forward(50)

#V-Line Lower Middle
v.penup()
v.goto(0, -50)
v.pendown()
v.forward(50)

#V-Line Lower Right
v.penup()
v.goto(50, -50)
v.pendown()
v.forward(50)


## Left Lines Code (variable "l")

#Left-Line Right
l.penup()
l.goto(50, -50)
l.pendown()
l.left(135)
l.forward(75)

#Left-Line Left
l.penup()
l.goto(0, -50)
l.pendown()
l.forward(75)

## Right-Line Code (variable "r")

#Right-Line Left
r.penup()
r.goto(-50, -50)
r.pendown()
r.left(40)
r.forward(38)

#Right-Line Left
r.penup()
r.goto(50, 0)
r.pendown()
r.right(180)
r.forward(38)

## Head-Line Code (variable "h")
#Start from (-50, 50)

#Left
h.penup()
h.setheading(0)
h.goto(-50, 50)
h.pendown()
h.left(45)
h.forward(75)

#Right
h.penup()
h.goto(50, 50)
h.pendown()
h.left(90)
h.forward(75)

##Butt-Line Code (variable "b")
#Start from (-50, -100)

#Left
b.penup()
b.setheading(0)
b.goto(-50, -100)
b.pendown()
b.right(45)
b.forward(75)

#Right
b.penup()
b.goto(50, -100)
b.pendown()
b.right(90)
b.forward(75)
