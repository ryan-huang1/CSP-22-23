# import turtle module
import random
import turtle as trtl

# create turtle object
painter = trtl.Turtle()
painter.speed(0)

# add code here for a circle
painter.circle(50)
painter.penup()

colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "black", "brown", "gray", "blue"]

cycle = 0
while True:
    painter.pendown()
    painter.circle(50)
    painter.right(2)
    painter.penup()
    cycle += 1

    current_cycle = cycle 
    while cycle == current_cycle:
        painter.color(colors[random.randint(0, len(colors)-1)])
        current_cycle += 1