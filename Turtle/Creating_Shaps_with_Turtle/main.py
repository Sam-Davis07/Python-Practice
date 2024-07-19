
import turtle

def creating_shape(sides,color):
    angle = round(360/sides)
    my_turtle.color(color)
    for i in range(sides):
        my_turtle.right(angle)
        my_turtle.forward(100)

my_turtle = turtle.Turtle()
my_screen = turtle.Screen()
my_turtle.pensize(15)

l1 = ['chartreuse','DarkOrchid','green','yellow','red','orange','blue','violet']

side = 3

while side <= 10 :
    for i in l1:
        creating_shape(side,i)
        side += 1
        
my_screen.exitonclick()

