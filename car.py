from turtle import Turtle
from random import choice, randint

color_list = [(255, 140, 0), (232, 17, 35), (104, 33, 122), (0, 188, 242), (0, 178, 148), (0, 158, 73), (186, 216, 10)]
MOVE_DISTANCE = 5
X_INIT = 300


class CarManager:
    def __init__(self):
        self.car_list = []

    def create_car(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.color(choice(color_list))
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        lane_nb = randint(-9, 9) * 25

        new_car.goto(x=X_INIT, y=lane_nb)
        self.car_list.append(new_car)

    def move(self, car):
        new_x = car.xcor() - MOVE_DISTANCE
        car.goto(x=new_x, y=car.ycor())
