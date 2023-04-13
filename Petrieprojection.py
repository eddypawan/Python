import turtle

# create a Turtle object
t = turtle.Turtle()

# set the speed of the turtle
t.speed(0)

# define a list of colors
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# loop through the list of colors and draw a circle with each color
for i in range(7):
    t.color(colors[i])
    t.circle(50)
    t.penup()
    t.forward(75)
    t.pendown()

# exit on click
turtle.exitonclick()
