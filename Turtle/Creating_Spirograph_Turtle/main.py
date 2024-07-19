import turtle
import random

my_turtle = turtle.Turtle()
my_scrren = turtle.Screen()

my_turtle.speed(0)

turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        my_turtle.color(random_color())
        my_turtle.circle(100)
        my_turtle.setheading(my_turtle.heading()+size_of_gap)

draw_spirograph(4)

my_scrren.exitonclick()