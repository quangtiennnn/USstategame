#turtle only work with gif type

import turtle as t
import pandas
from score import Score
"""SCREEN"""
mouse = t.Turtle()
mouse.penup()
mouse.hideturtle()
screen = t.Screen()
screen.title("U.S States Name")
screen.setup(width = 360*2,height=245*2)
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)
score = Score()
"""DATA"""
data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()
data_dict = {}
for i in range(len(state_list)):
    data_dict[state_list[i]] = (data["x"][i],data["y"][i])
"""GUESS"""
game_is_on = True
while game_is_on:
    guess = screen.textinput(title="U.S State:",prompt="Name the State")
    if guess in state_list:
        state_list.remove(guess)
        mouse.goto(data_dict[guess])
        mouse.write(guess)
        score.score += 1
        score.write_score()
    else:
        game_over = t.Turtle()
        game_over.hideturtle()
        game_over.write("Game Over!!",align="center",font=('Arial', 15, 'normal'))
        state_to_learn = pandas.DataFrame(state_list)
        state_to_learn.to_csv("state_to_learn.csv")
        game_is_on = False

screen.exitonclick()