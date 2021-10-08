from turtle import Turtle, Screen
import time

STARTING_POSITIONS = [(-20, 0), (0, 0), (20, 0)]


# class Snake:
#
#     def __init__(self):
#         self.X = -20
#         self.Y = 0
#         self.segments = []
#         for position in STARTING_POSITIONS:
#             self.add_segment(position)
#         self.head = self.segments[2]
#
#     def add_segment(self, position):
#         new_segment = Turtle(shape="square")
#         new_segment.color("white")
#         new_segment.penup()
#         # position = (self.X, self.Y)
#         new_segment.goto(position)
#         self.segments.append(self.new_segment)
#         # self.X += 20


screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("My  fake Snake Game")
screen.tracer(0)

segments = []

for position in STARTING_POSITIONS:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

# snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

screen.exitonclick()
