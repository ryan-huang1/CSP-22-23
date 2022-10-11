#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  #turle color
  new_color = turtle_colors.pop()
  t.fillcolor(new_color)
  t.penup()
  my_turtles.append(t)

#  
startx = 0
starty = 0 

past_heading = 90

#
for t in my_turtles:
  t.goto(startx, starty)
  t.setheading(past_heading)
  t.pendown()
  t.right(45)
  t.forward(50)

#	
  startx = t.xcor()
  starty = t.ycor()
  past_heading = t.heading()

wn = trtl.Screen()
wn.mainloop()