from turtle import Turtle

Y = 280
X = 0
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class PlayBoard:

    def __init__(self):
        self.FORWARD = 570
        self.line = Turtle()
        self.line.color("white")
        self.line.hideturtle()
        self.line.penup()
        self.line.goto(x=X, y=Y + 10)
        self.line.setheading(270)
        while self.FORWARD > 0:
            self.line.pendown()
            self.line.forward(20)
            self.FORWARD -= 20
            self.line.penup()
            self.line.forward(20)
            self.FORWARD -= 20


class Score(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.write(self.score, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(self.score, align=ALIGNMENT, font=FONT)
