## used to extract colors
# import colorgram
# colors = colorgram.extract('image.jpg', 30)

# rgb_list = []

# for color in colors:
#     rgb = (color.rgb.r, color.rgb.g, color.rgb.b)
#     rgb_list.append(rgb)

import turtle as t
import random

color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim = t.Turtle()
screen = t.Screen()
t.colormode(255)
tim.speed("fastest")
tim.pu()
tim.hideturtle()

tim.setpos(-200, -200)
for j in range(1, 11):
    for i in range(10):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)
        tim.pd()
    tim.pu()    
    tim.setpos(-200, -200 + 50 * j)
screen.exitonclick()