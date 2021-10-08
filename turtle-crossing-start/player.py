from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
MOVE_INCREMENT = 0.5


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.move_speed = MOVE_INCREMENT

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() == FINISH_LINE_Y:
            return True

    def refresh(self):
        self.goto(STARTING_POSITION)
        self.move_speed *= MOVE_INCREMENT

