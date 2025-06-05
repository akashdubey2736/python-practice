from turtle import Turtle,Screen,colormode
import random

colormode(255)

tim=Turtle()
tim.speed("fastest")
screen=Screen()


def random_color():
    r=random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color=(r,g,b)
    return color



def draw_spirograph(size_of_gap):
    for val in range(int(360/size_of_gap)):
        tim.pencolor(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)

draw_spirograph(5)
screen.exitonclick()




