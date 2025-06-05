from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.shapesize(stretch_wid=2,stretch_len=2)
        self.go_to_start()
        self.setheading(90)


    def move_turtle(self):
        self.forward(10)

    def go_to_start(self):
        self.goto(0,-280)
