# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl

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

spot_painter = trtl.Turtle()
spot_painter.shape("circle")
spot_painter.shapesize(spot_size)
spot_painter.fillcolor(spot_color)

triangle_painter = trtl.Turtle()
triangle_painter.shape("triangle")
triangle_painter.shapesize(triangle_size)
triangle_painter.fillcolor(triangle_color)

square_painter = trtl.Turtle()
square_painter.shape("square")
square_painter.shapesize(square_size)
square_painter.fillcolor(square_color)

classic_painter = trtl.Turtle()
classic_painter.shape("classic")
classic_painter.shapesize(classic_size)
classic_painter.fillcolor(classic_color)

wn = trtl.Screen()

#-----game configuration----


#-----initialize turtle-----


#-----game functions--------


#-----events----------------

wn = trtl.Screen()
wn.mainloop()