# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----

spot_color = "pink"
spot_size = 2
spot_shape= "circle"

triangle_color = "blue"
triangle_size = 2
triangle_shape = "triangle"

square_color = "green"
square_size = 3
square_shape = "square"

classic_color = "red"
classic_size = 1
classic_shape = "classic"

#-----initialize turtle-----

spot_painter = trtl.Turtle()
spot_painter.shape("circle")
spot_painter.shapesize(spot_size)
spot_painter.fillcolor(spot_color)

# triangle_painter = trtl.Turtle()
# triangle_painter.shape("triangle")
# triangle_painter.shapesize(triangle_size)
# triangle_painter.fillcolor(triangle_color)

# square_painter = trtl.Turtle()
# square_painter.shape("square")
# square_painter.shapesize(square_size)
# square_painter.fillcolor(square_color)

# classic_painter = trtl.Turtle()
# classic_painter.shape("classic")
# classic_painter.shapesize(classic_size)
# classic_painter.fillcolor(classic_color)

#-----game functions--------

def spot_clicked(x, y):
    print("spot clicked")
    change_position()

def change_position():
    spot_painter.penup()
    spot_painter.hideturtle()
    spot_painter.goto(rand.randint(-350,350), rand.randint(-250,250))
    spot_painter.showturtle()
    spot_painter.pendown()

#-----events----------------

spot_painter.onclick(spot_clicked)
wn = trtl.Screen()
wn.mainloop()