## Make turtle run initials fo JAG

#Turtle assignments to different letters 

import turtle

window = turtle.Screen()
window.bgcolor("yellow")

j = turtle.Turtle()
j.color("red")
j.shape("turtle")

a = turtle.Turtle()
a.color("green")
a.shape("triangle")

g = turtle.Turtle()
g.color("blue")
g.shape("circle")

#movement patterns for J
j.goto(-100, 0)
j.forward(100)
j.backward(50)
j.right(90)
j.forward(100)
j.right(90)
j.forward(75)


#movement patterns for A
a.penup()
a.goto(50, 0)
a.pendown()
a.right(65)
a.forward(100)
a.backward(50)
a.right(115)
a.forward(50)
a.right(115)
a.forward(60)
a.backward(110)


#movement pattern for g

           
