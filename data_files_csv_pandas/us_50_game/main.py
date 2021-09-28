import turtle
import pandas
import random

screen = turtle.Screen()
screen.title("US 50 States Game")
img_path = "blank_states_img.gif"
screen.addshape(img_path)
turtle.shape(img_path)

correct_states_map = {}
correct_states_count = 0
while correct_states_count < 50:
    answer_state = screen.textinput(title="Guess a state", prompt="what is the state?")
    if answer_state is None or answer_state == "Exit":
        break
    data = pandas.read_csv("50_states.csv")
    state_data = data[data.state == answer_state]
    if len(state_data.state) < 1:
        continue
    if correct_states_map.get(answer_state):
        continue
    correct_states_map[answer_state] = (int(state_data.x.item()), int(state_data.y))
    correct_states_count += 1
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(int(state_data.x), int(state_data.y))
    t.write(state_data.state.item())


all_states=data["state"].to_list()
missing_states=[state for state in all_states if not correct_states_map.get(state)]

missing_states_data=pandas.DataFrame(missing_states)
missing_states_data.to_csv(f"missing_states_{random.randint(0,1000)}.csv")

