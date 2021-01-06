from turtle import Screen
import time
from player import Player
from car import CarManager
from random import randint
from scoreboard import ScoreBoard, GameOver, FinishLine

screen = Screen()
screen.setup(height=int(600), width=int(600))
screen.title("Cross the Road")
screen.tracer(0)
screen.colormode(255)

#TODO: 1. Create turtle
tim = Player()
#TODO: 5. Create Level tracker and general board
scoreboard = ScoreBoard()
endgame = GameOver()
finishline = FinishLine()

#TODO: 3. Create cars
carmanager = CarManager()

#TODO: 2. Turtle behaviour
screen.listen()
screen.onkeypress(tim.up,"Up")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(scoreboard.difficulty)
#Generate a car 1 time every 6 refresh on average
    # TODO: 4. Create car behaviour
    if randint(0,6) == 1:
        carmanager.create_car()
#Make the generated cars move
    for car in carmanager.car_list:
        carmanager.move(car)
        # TODO: 7. When turtle collides, game is over
        if tim.distance(car) < 20:
            game_is_on = False
            endgame.game_is_over()
    # TODO: 6. Increase level
    if tim.ycor() > finishline.ycor()+5:
        tim.new_level()
        scoreboard.increase()







screen.exitonclick()


