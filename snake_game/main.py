import time
from turtle import Screen
from snake import Snake
from snake_game.food import Food
from snake_game.scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()


    if snake.head.distance(food) <  15:
        food.refresh()
        snake.extend_turtle()
        scoreboard.increase_score()
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        scoreboard.reset()
        snake.reset()

    for turtle in snake.turtle_list[1:]:
        if snake.head.distance(turtle)<10:
            scoreboard.reset()
            snake.reset()



screen.exitonclick()