from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.level = 1
        self.difficulty = 0.1

        self.penup()
        self.goto(x=-240, y=270)
        self.color("black")
        self.update()
        self.ht()

    def update(self):
        self.write(arg=f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.level += 1
        self.difficulty *= 0.8
        self.clear()
        self.update()

class GameOver(ScoreBoard):
    def __init__(self):
        super().__init__()

        self.goto(x=0, y=0)

    def update(self):
        pass

    def game_is_over(self):
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

class FinishLine(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.goto(x=-300, y=240)
        self.pendown()
        self.goto(x=300,y=240)
        self.ht()
