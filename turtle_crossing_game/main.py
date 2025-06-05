import time
from turtle import Turtle,Screen

from turtle_crossing_game.player import Player
from turtle_crossing_game.car_manager import CarManager
from turtle_crossing_game.scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Turtle Crossing")
screen.tracer(0)
game_is_on=True

player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()


screen.listen()
screen.onkey(player.move_turtle,"Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on=False

    if player.ycor()>280:
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()



screen.exitonclick()