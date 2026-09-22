import turtle
from turtle import Turtle , Screen
import random
#spirograph

timmy = Turtle()
turtle.colormode(255)
#
def random_color():
     r = random.randint(0, 255)
     g = random.randint(0, 255)
     b = random.randint(0, 255)
     color = (r, g, b)
     timmy.color(color)
#
# directions = [0, 90, 180, 270]
timmy.speed("fastest")
# timmy.pensize(15)
#
# for _ in range(200):
#     random_color()
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))

#OR
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        random_color()
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)
draw_spirograph(5)
screen = Screen()
screen.exitonclick()
