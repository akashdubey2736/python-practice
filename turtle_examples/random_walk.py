import random
from turtle import Turtle,colormode

tim=Turtle()
tim.width(10)
colormode(255)

def random_color():
    r=random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color=(r,g,b)
    return color

no_of_steps=random.randint(1,101)
directions=[0,90,180,270]

while no_of_steps>0:
    tim.color(random_color())
    tim.forward(20)
    tim.setheading(random.choice(directions))
    no_of_steps-=1

