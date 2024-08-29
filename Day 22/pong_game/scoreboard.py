from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.score_update()

    def score_update(self):
        self.goto(-100, 200)
        self.write(arg=self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(arg=self.r_score, align=ALIGNMENT, font=FONT)

    def increase_l_score(self):
        self.l_score += 1
        self.clear()
        self.score_update()

    def increase_r_score(self):
        self.r_score += 1
        self.clear()
        self.score_update()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)
