import turtle
import pandas


# PROPERTIES
screen = turtle.Screen()
screen.title("U.S. States Game")

bg_img = "blank_states_img.gif"
screen.addshape(bg_img)
turtle.shape(bg_img)

df = pandas.read_csv("50_states.csv")
states = df.state.to_list()

guessed_states = []
game_is_in_progress = len(guessed_states) < 50


# METHODS
def save_states_to_learn(states, guessed_states):
    missing_states = [state for state in states if state not in guessed_states]
    new_df = pandas.DataFrame(missing_states)
    new_df.to_csv("states_to_learn.csv")


# MAIN
while game_is_in_progress:
    res = screen.textinput(f"{len(guessed_states)}/50 States Correct", "Guess a state name").title()

    if res in states:
        guessed_states.append(res)

        state = turtle.Turtle()
        state.penup()
        state.hideturtle()

        state_data = df[df.state == res]
        state.goto(int(state_data.x), int(state_data.y))
        state.write(state_data.state.item(), align="center", font=("Arial", 12, "normal"))

    if res == "Exit":
        save_states_to_learn(states, guessed_states)
        break
