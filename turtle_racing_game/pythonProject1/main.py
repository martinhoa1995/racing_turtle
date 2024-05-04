from turtle import Turtle, Screen
import random

screen = Screen()
is_race_on = True
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race?: ")
colore_list = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-90, -50, -20, 20, 50, 90]
turtle_list = []

for turtle_index in range(6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.speed("slowest")
    tim.color(colore_list[turtle_index])
    tim.goto(x=-230, y=y_position[turtle_index])
    turtle_list.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for tim in turtle_list:
        if tim.xcor() >= 230:
            is_race_on = False
            winning_color = tim.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        tim.forward(rand_distance)

screen.exitonclick()
