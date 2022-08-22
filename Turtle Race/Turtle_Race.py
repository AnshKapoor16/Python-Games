from turtle import Turtle, Screen
import random

is_race = False
screen = Screen()
screen.setup(width = 500, height = 400)
bet = screen.textinput(title="Make a Bet!", prompt="Which color turtle will win the race? Enter color: ")
colors = ["red", "blue", "green", "orange", "yellow", "purple"]
y_pos = [-100,-60,-20,20,60,100]
all_turtles = []

for index in range(0,6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.goto(-235, y_pos[index])
    tim.color(colors[index])
    all_turtles.append(tim)

if bet:
    is_race = True

while is_race:

    for turtle in all_turtles:        
        if turtle.xcor() <= 240:
            turtle.forward(random.randint(0,10))
        
        if turtle.xcor() > 230:
            is_race = False
            win_color = turtle.pencolor()
            if win_color == bet:
                print(f"You've Won! The {win_color} turtle is the winner")
            else:
                print(f"You've Lost! The {win_color} turtle is the winner")



screen.exitonclick()