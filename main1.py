from turtle import Turtle, Screen
#
import random
from turtle import Turtle, Screen
#
timmy = Turtle()
screen = Screen()
#
# List of color names supported by Turtle
colors = [
     "CornflowerBlue", "DarkOrchid", "IndianRed",
     "DeepSkyBlue", "LightSeaGreen", "wheat",
     "SlateGray", "SeaGreen"
 ]
#
# number_of_sides = 3
#
#
# def draw_shape(num_sides):
#     turn_angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(turn_angle)
#
#
# while number_of_sides <= 10:
#     # 1. Select and set a random color before drawing
#     timmy.color(random.choice(colors))
#
#     # 2. Draw the polygon
#     draw_shape(number_of_sides)
#
#     # 3. Move to the next shape
#     number_of_sides += 1
def timmy_walk_right():
    timmy.color(random.choice(colors))
    timmy.forward(20)
    timmy.right(90)

def timmy_walk_left():
    timmy.color(random.choice(colors))
    timmy.forward(20)
    timmy.left(90)
def timmy_walk_up():
    timmy.color(random.choice(colors))
    timmy.forward(20)

timmy.speed(0)
timmy.width(10)
timmy_random_walk  = [timmy_walk_left, timmy_walk_right, timmy_walk_up]
# for _ in range(200):
#     random_walk = random.choice(timmy_random_walk)
#     random_walk()
#or instead of all this simply do this
directions = [0, 90, 180, 270]

for _ in range(200):
    timmy.color(random.choice(colors))
    timmy.setheading(random.choice(directions))
    timmy.forward(30)
screen.exitonclick()