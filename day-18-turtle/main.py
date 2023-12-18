from turtle import Turtle, Screen
import random
import turtle

timmy = Turtle()
timmy.shape("arrow")
timmy.color("black")

# # Draw a square
# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)

screen = Screen()

# Drawing a dashed line
# for i in range(20):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

colours = ["light cyan", "pink", "lavender blush", "lavender", "peach puff", "lemon chiffon", "honeydew", "misty rose"]
direction = [0, 90, 180, 270]

# for n_sides in range(3, 11):
#     timmy.setheading(0)
#     timmy.color(random.choice(colours))
#     angle = 360 / n_sides
    
#     for j in range(n_sides):
#         timmy.forward(100)
#         timmy.right(angle)

# turtle.colormode(255)

# def random_color_rgb():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
    
#     return (r, g, b)

# timmy.pensize(10)
timmy.speed("fastest")
# for i in range(200):
#     timmy.pencolor(random_color_rgb())
#     timmy.setheading(random.choice(direction))
#     timmy.forward(25)

for i in range(36):
    timmy.circle(100)
    timmy.pencolor(random.choice(colours))
    timmy.setheading(timmy.heading() + 10)
    




screen.exitonclick()


