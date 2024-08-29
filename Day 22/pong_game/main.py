from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(fun=right_paddle.go_up, key="Up")
screen.onkey(fun=right_paddle.go_down, key="Down")
screen.onkey(fun=left_paddle.go_up, key="w")
screen.onkey(fun=left_paddle.go_down, key="s")
game_on = True


while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect the collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_hit()

    # stop the game
    if scoreboard.l_score == 10 or scoreboard.r_score == 10:
        game_on = False
        scoreboard.game_over()
    else:
        # Detect R paddle miss
        if ball.xcor() > 400:
            # game_on = False
            # scoreboard.game_over()
            ball.reset_position()
            scoreboard.increase_l_score()

        # Detect L paddle miss
        if ball.xcor() < -400:
            ball.reset_position()
            scoreboard.increase_r_score()




screen.exitonclick()
