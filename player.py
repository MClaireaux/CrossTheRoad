from turtle import Turtle
STEP = 20
X_INIT=0
Y_INIT=-280

class Player(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.penup()
        self.goto(x=X_INIT, y=Y_INIT)
        self.setheading(90)

    def up(self):
        new_y = self.ycor() + STEP
        self.goto(x=X_INIT, y=new_y)

    def new_level(self):
        self.goto(x=X_INIT, y=Y_INIT)