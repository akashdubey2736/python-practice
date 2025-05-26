from turtle import Turtle, Screen

tim=Turtle()
screen=Screen()
for value in range(10):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
screen.exitonclick()

