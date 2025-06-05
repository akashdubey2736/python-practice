import random
from turtle import Turtle, Screen, colormode

colormode(255)

'''
import colorgram
colors=colorgram.extract('image.jpg',30)
rgb_colors=[]
for color in colors:
    r=color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color=(r,g,b)
    rgb_colors.append(new_color)
 '''
colors=[(246, 245, 245), (25, 42, 64), (130, 165, 207), (233, 149, 89), (206, 135, 147),
        (239, 210, 83), (194, 217, 236), (133, 184, 161), (27, 111, 168), (174, 59, 44),
        (157, 32, 30), (51, 39, 42), (177, 27, 30), (140, 67, 78), (38, 61, 54), (238, 209, 217),
        (239, 164, 152), (231, 163, 167), (51, 122, 107), (221, 79, 71), (1, 104, 73), (23, 62, 119),
        (197, 100, 109), (17, 83, 107), (61, 55, 51), (196, 222, 219), (110, 126, 151),
        (169, 204, 192), (91, 146, 137)]

tim=Turtle()
tim.speed("fastest")
tim.penup()
screen=Screen()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_steps=100

for val in range(1,number_of_steps+1):
    tim.dot(20,random.choice(colors))
    tim.forward(50)

    if val % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen.exitonclick()


