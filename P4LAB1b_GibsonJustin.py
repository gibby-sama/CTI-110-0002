#start turtle graphics
import turtle

#define window color
window = turtle.Screen()
window.bgcolor("sky blue")

#define turle, shap & color
t = turtle.Turtle()
t.shape("turtle")
t.fillcolor("crimson")

#draw j
t.forward(100)
t.penup()
t.goto(50,0)
t.pendown()
t.right(90)
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)


#draw g
t.penup()
t.goto(200,0)
t.pendown()
t.right(90)
t.forward(100)
t.goto(200,0)
t.right(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)

##Easy way

##import turtle
##
### Function to set turtle properties
##def set_turtle_properties(color, pen_size):
##    turtle.pencolor(color)
##    turtle.pensize(pen_size)
##
### Function to draw an initial
##def draw_initial(initial, pen_up_distance):
##    turtle.write(initial, font=("Arial", 36, "normal"))
##    turtle.penup()
##    turtle.forward(pen_up_distance)
##    turtle.pendown()
##
### Main function
##def main():
##    # Set up turtle properties
##    set_turtle_properties("blue", 5)
##
##    # Draw first initial "J"
##    draw_initial("J", 50)
##
##    # Draw second initial "G"
##    draw_initial("G", 50)
##
##    # Close the turtle graphics window on click
##    turtle.exitonclick()
##
### Run the program
##if __name__ == "__main__":
##    main()
##           
