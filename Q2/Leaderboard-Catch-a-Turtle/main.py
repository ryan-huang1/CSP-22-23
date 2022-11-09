# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb

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

leaderboard_file_name = "a122_leaderboard.txt"
player_name = input("Please enter your name: ")

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

def manage_leaderboard():

  global score
  global spot

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, spot, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, spot, score)

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
    manage_leaderboard()
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
wn.bgcolor("sky blue")
wn.ontimer(countdown, counter_interval) 
wn.mainloop()