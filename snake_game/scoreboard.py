import turtle
from turtle import Turtle

from max_number import score



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,278)
        self.update_scoreboard()


    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("data.txt","w") as data:
                data.write(f"{self.high_score}")
        self.score=0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}", align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
       self.score+=1
       self.update_scoreboard()

   # def game_over(self):
   #     self.goto(0,0)
   #     self.write("Game Over!!", align="center", font=("Courier", 24, "normal"))






