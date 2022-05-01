import turtle
import pandas

# Sets up screen using Turtle module
screen = turtle.Screen()
screen.title("U.S. States Game")

#Setup the Image on the screen
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#setup variables
score = 0

#reads 50 states from csv file and creates a dictionary of the data. Then creates a list of the name of the States
data = pandas.read_csv("50_states.csv")
data_dict = data.to_dict()
all_states = data.state.to_list()

#create list to hold guessed states
guessed_states = []

#main loop that checks to see if all 50 states have been guessed and if not keeps asking for a new entry.
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another State's name?")
    answer_state = answer_state.title()

    #way to end the game
    if answer_state == "Exit":
        break

    #looks to see if the chosen state is on the list of states. if so gets x and y coordinates and adds state to guessed states.
    if all_states.index(answer_state):
        state_chosen = all_states.index(answer_state)
        state_x = data.at[state_chosen, 'x']
        state_y = data.at[state_chosen, 'y']
        guessed_states.append(answer_state)

        #create turtle to name state on map
        t = turtle.Turtle()
        t.penup()
        t.color("Black")
        t.hideturtle()
        t.goto(x=state_x, y=state_y)
        t.write(data.at[state_chosen, 'state'])

#creates csv with states that were not guessed so user can learn them.
unknown_states = [state for state in data.state if state not in guessed_states]
dict = {'States to Learn': unknown_states}
df = pandas.DataFrame(dict)
df.to_csv('states_to_learn.csv')

screen.exitonclick()