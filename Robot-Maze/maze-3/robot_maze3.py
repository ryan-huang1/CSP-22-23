#   a115_robot_maze.py
import turtle as trtl

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

#------ robot commands
def move():
  robot.dot(10)
  robot.fd(50)

def turn_left():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)

#----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "/Users/ryanhuang/Documents/GitHub/CSP-22-23/Robot-Maze/robot_1_40x50.gif"
wn.addshape(robot_image)

#----- init robot
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()

# #---- TODO: change maze here
wn.bgpic("/Users/ryanhuang/Documents/GitHub/CSP-22-23/Robot-Maze/maze-3/maze3.png") # other file names should be maze2.png, maze3.png

#---- TODO: begin robot movement here
# move robot forward with move()
# turn robot left with turn_left()
# sample for loop:
'''
for step in range(3): # forward 3
  move()
'''
cycle = 0 
one = 0
two = 0
three = 0
while cycle == 0:
  while one == 0:
    robot.setheading(0)
    move()
    robot.setheading(90)
    for i in range(2):
      move()
    robot.setheading(0)
    move()
    one += 1

  robot.color("blue")
  robot.pencolor("blue")
  
  while two == 0:
    robot.setheading(90)
    move()
    robot.setheading(0)
    for i in range(2):
      move()
    robot.setheading(90)
    move()
    two += 1

#---- end robot movement 

wn.mainloop()
