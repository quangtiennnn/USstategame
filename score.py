from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(0, 220)
        self.score = 0
    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}/50", align="center",font=('Arial', 15, 'normal'))