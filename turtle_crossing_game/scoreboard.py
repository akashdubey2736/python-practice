from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-240,250)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"level : {self.level}", align="center", font=("Courier", 20, "bold"))


    def increase_level(self):
        self.level+=1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!!", align="center", font=("Courier", 20, "bold"))