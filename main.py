import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Quiz")

map_img = "blank_states_img.gif"
screen.addshape(map_img)
turtle.shape(map_img)
data = pandas.read_csv("50_states.csv")
list_states = data.state.tolist()

done = False
correct_answers = 0
while not done:

    answer = screen.textinput(title=f"{correct_answers}/50 Correct States",
                              prompt="What's another state that you haven't mentioned yet")
    answer = answer.title()

    if answer in list_states:
        correct_answers += 1
        list_states.remove(answer)
        state_name = turtle.Turtle()
        state_name.ht()
        state_name.penup()
        location = data[data.state == answer]
        x_location = int(location.x.values[0])
        y_location = int(location.y.values[0])
        state_name.goto(x_location, y_location)
        state_name.write(arg=answer, align="center", font=("Arial", 8, "bold"))

        if correct_answers == 50:
            done = True

screen.mainloop()

