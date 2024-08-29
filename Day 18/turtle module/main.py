import turtle
import random
from turtle import Turtle, Screen  # or from turtle import * # import turtle as t which mean alias name

turtle.colormode(255)
timmy = Turtle()
timmy.shape("turtle")


# timmy.color("black", "green")

# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)

# for _ in range(10):
#     timmy.pendown()
#     timmy.forward(20)
#     timmy.penup()
#     timmy.forward(20)


# points = 3
# limit = 11
# keep_going = True
# colors = ["DeepSkyBlue", "LightSkyBlue", "PaleGoldenrod", "LightPink", "CornflowerBlue", "LightSteelBlue", "LightGreen", "NavajoWhite"]
# while keep_going:
#     if points != limit:
#         for _ in range(points):
#             turn = 360 / points
#             timmy.forward(100)
#             timmy.right(turn)
#         points += 1
#         timmy.color(random.choice(colors))
#     else:
#         keep_going = False

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors


# directions = [0, 90, 180, 270]
# timmy.width(13)
# timmy.speed("fastest")
# for _ in range(200):
#     timmy.color(random_color())
#     steps = int(random.random() * 80)
#     timmy.forward(steps)
#     timmy.setheading(random.choice(directions))

# my way V
# timmy.width(1)
# rounds = 5.0
# timmy.speed("fastest")
# for _ in range(100):
#     timmy.circle(100)
#     timmy.left(rounds)
#     rounds += 0.1
#     print(rounds)
#     timmy.color(random_color())

# course way V
timmy.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
