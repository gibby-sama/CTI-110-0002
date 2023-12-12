import turtle

# Set up turtle properties for the triangle
triangle_turtle = turtle.Turtle()
triangle_turtle.pencolor("green")
triangle_turtle.pensize(3)

# Draw a triangle
for t in range(3):
    triangle_turtle.forward(100)
    triangle_turtle.left(120)

# Move turtle to start drawing the square
triangle_turtle.penup()
triangle_turtle.forward(150)  # Move to the right to start the square
triangle_turtle.pendown()

# Set up turtle properties for the square
square_turtle = turtle.Turtle()
square_turtle.pencolor("blue")
square_turtle.pensize(3)

# Draw a square
for t in range(4):
    square_turtle.forward(100)
    square_turtle.left(90)
