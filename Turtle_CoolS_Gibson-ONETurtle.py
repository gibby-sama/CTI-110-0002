import turtle

window = turtle.Screen()
window.bgcolor("sky blue")

v = turtle.Turtle()
v.speed(speed=5)
v.shape("turtle")
v.fillcolor("crimson")

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


## Left Lines Code 

#Left-Line Right
v.penup()
v.setheading(0)
v.goto(50, -50)
v.pendown()
v.left(135)
v.forward(75)

#Left-Line Left
v.penup()
v.goto(0, -50)
v.pendown()
v.forward(75)

## Right-Line Code

#Right-Line Left
v.penup()
v.setheading(0)
v.goto(-50, -50)
v.pendown()
v.left(40)
v.forward(38)

#Right-Line Right
v.penup()
v.goto(50, 0)
v.pendown()
v.right(180)
v.forward(38)

## Head-Line Code 
#Start from (-50, 50)

#Left
v.penup()
v.setheading(0)
v.goto(-50, 50)
v.pendown()
v.left(45)
v.forward(72)

#Right
v.penup()
v.goto(50, 50)
v.pendown()
v.left(90)
v.forward(72)

##Butt-Line Code
#Start from (-50, -100)

#Left
v.penup()
v.setheading(0)
v.goto(-50, -100)
v.pendown()
v.right(45)
v.forward(73)

#Right
v.penup()
v.goto(50, -100)
v.pendown()
v.right(90)
v.forward(73)

v.penup()
v.goto(-300, -300)

v.hideturtle()
