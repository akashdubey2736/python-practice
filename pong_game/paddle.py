from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,x_pos,y_pos):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(x_pos, y_pos)


    def go_up(self):
        new_y=self.ycor()+10
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y=self.ycor()-10
        self.goto(self.xcor(),new_y)