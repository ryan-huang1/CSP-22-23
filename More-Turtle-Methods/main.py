# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()

# add code here for a circle
painter.circle(50)
painter.penup()

# move the turtle to another part of the screen
painter.goto(100, 100)

# add code here for an arc
painter.pendown()
painter.circle(100, 180)
painter.penup()

# move the turtle to another part of the screen
painter.goto(150, 150)

# add code here for an arc that is greater than 90 degrees and has 5 steps
painter.pendown()
painter.circle(100, 180, 5)
painter.penup()

# move the turtle to another part of the screen
painter.goto(-100, -100)

# add code here to create a polygon of your choice using the circle method
painter.pendown()
painter.circle(50, 360, 5)
painter.penup()

# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()