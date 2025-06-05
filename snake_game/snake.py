from turtle import Turtle,Screen

STARTING_POSITION=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.turtle_list=[]
        self.create_snake()
        self.head=self.turtle_list[0]

    def create_snake(self):
        for turtle_index in STARTING_POSITION:
            self.add_turtle(turtle_index)


    def add_turtle(self,turtle_index):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(turtle_index)
        self.turtle_list.append(new_turtle)

    def reset(self):
        for snake in self.turtle_list:
            snake.goto(1000,1000)
        self.turtle_list.clear()
        self.create_snake()
        self.head = self.turtle_list[0]

    def extend_turtle(self):
        self.add_turtle(self.turtle_list[-1].position())

    def move(self):
        for turtle in range(len(self.turtle_list) - 1, 0, -1):
            new_x = self.turtle_list[turtle - 1].xcor()
            new_y = self.turtle_list[turtle - 1].ycor()
            self.turtle_list[turtle].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading()!= LEFT:
            self.head.setheading(RIGHT)
