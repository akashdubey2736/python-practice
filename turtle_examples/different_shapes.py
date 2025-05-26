from turtle import Turtle, Screen

tim=Turtle()
screen=Screen()
colors=["red","blue","green","orange","purple","yellow","pink","grey","black","olive"]

for value  in range (3,11):
    tim.color(colors[value-1])
    for val in range(1,value+1):
        tim.forward(50)
        tim.right(360/value)
        tim.forward(50)


screen.exitonclick()