# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----

score = 0

font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

spot_color = "pink"
spot_size = 2
spot_shape= "circle"

#-----initialize turtle-----

spot_painter = trtl.Turtle()
spot_painter.shape("circle")
spot_painter.shapesize(spot_size)
spot_painter.fillcolor(spot_color)

counter =  trtl.Turtle()
counter.penup()
counter.goto(-350, 300)

score_writer = trtl.Turtle()
score_writer.penup()
score_writer.goto(-350, 250)
score_writer.write(score, font=font_setup)

#-----game functions--------

def update_score():
    global score
    score += 1
    print(score)
    score_writer.clear()
    score_writer.write(score, font=font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

def spot_clicked(x, y):

    global timer_up
    if not timer_up:
        print("spot clicked")
        change_position()
        update_score()
    else:
        spot_painter.hideturtle()

def change_position():
    spot_painter.penup()
    spot_painter.hideturtle()
    spot_painter.goto(rand.randint(-350,350), rand.randint(-250,250))
    spot_painter.showturtle()
    spot_painter.pendown()

#-----events----------------

spot_painter.onclick(spot_clicked)
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval) 
wn.mainloop()