from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.level_update()

    def level_update(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.level_update()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align="center", font=FONT)
