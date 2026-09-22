from turtle import Turtle , Screen
import random
screen = Screen()
screen.colormode(255)
# import colorgram
# colors = colorgram.extract("Addictive---detail-of-Dam-007.jpeg",30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)
colors_list = [(203, 165, 109), (150, 72, 48), (239, 245, 240), (232, 235, 241), (222, 202, 137), (171, 152, 41), (52, 93, 124), (135, 32, 23), (133, 162, 184), (198, 92, 72), (49, 123, 90), (14, 98, 74), (146, 178, 147), (69, 49, 41), (234, 176, 166), (162, 142, 157), (55, 45, 50), (150, 19, 23), (113, 75, 77), (185, 205, 174), (22, 82, 86), (48, 65, 81), (45, 61, 73), (90, 144, 126), (219, 177, 181), (108, 127, 154), (194, 83, 86), (178, 190, 208)]
timmy = Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()  # Hide the turtle icon for a cleaner look

# Grid configuration
start_x = -225
start_y = -225
spacing = 50
dot_size = 20

# Nested loop to create a 10x10 grid
for row in range(10):
    # Position turtle at the start of the current row
    timmy.goto(start_x, start_y + (row * spacing))

    for col in range(10):
        # Pick a random color and draw a dot
        timmy.dot(dot_size, random.choice(colors_list))
        timmy.forward(spacing)

screen.exitonclick()






screen.exitonclick()