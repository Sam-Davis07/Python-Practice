from turtle import *

my_turtle = Turtle()
my_screen = Screen()

for i in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)
my_turtle.hideturtle()
my_screen.exitonclick()