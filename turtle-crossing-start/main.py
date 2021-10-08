import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(fun=player.move_forward, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(player.move_speed)
    print(player.move_speed)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            score_board.game_over()
            game_is_on = False

    if player.is_at_finish_line():
        player.refresh()
        score_board.add_level()

screen.exitonclick()
