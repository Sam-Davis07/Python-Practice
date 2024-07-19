import turtle
import random

my_turtle = turtle.Turtle()
my_screen = turtle.Screen()
turtle.colormode(255)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(255)
    random_color = (r,g,b)
    return random_color
    
    
my_turtle.pensize(15)
my_turtle.speed(0)

angle = [0,90,180,270,360]

def random_walk():
    my_turtle.color(random_color())
    my_turtle.setheading(random.choice(angle))
    my_turtle.forward(30)
    
# my_turtle.right(0)  East
# my_turtle.right(90)   South
# my_turtle.right(180)  West
# my_turtle.right(270)  North
# my_turtle.right(360)  East

# colors =["chartreuse","cyan","dark orchid","medium violet red","blue violet","medium blue","lime green","firebrick","dark orange"]

for i in range(200):
    random_walk()



my_screen.exitonclick()
