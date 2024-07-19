
import turtle

my_turtle = turtle.Turtle()
my_screen = turtle.Screen()

for i in range(15):
    my_turtle.forward(10)
    my_turtle.penup()
    my_turtle.forward(10)
    my_turtle.pendown()

my_screen.exitonclick()


