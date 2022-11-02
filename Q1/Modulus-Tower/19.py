#   a113_tower.py
#   Modify this code in VS Code to alternate the colors of the 
#   floors every three floors
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of the tower
x = -150
y = -150

# height of tower and a counter for each floor
num_floors = 63

# iterate
for floor in range(num_floors):
  var = floor % 21
  if var == 0:
    x = x + 100
    y = -150

  # set placement and color of turtle
  painter.penup()
  painter.goto(x, y)
  rem = floor % 6
  if (rem > 2):  
    painter.color("blue")
  else:
    painter.color("grey")
  y = y + 5 # location of next floor
   
  #draw the floor
  painter.pendown()
  painter.forward(50)

wn = trtl.Screen()
wn.mainloop()