from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Snake start eating
    if snake.head.distance(food) < 15:
        food.new_food_location()
        snake.extend()
        scoreboard.increase_score()

    # collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

    # collision with tail
    for square in snake.squares[1:]:
        if snake.head.distance(square) < 10:
            game_on = False
            scoreboard.game_over()


screen.exitonclick()
