import time
from turtle import Screen, penup
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(player.move, 'Up')

scoreboard = Scoreboard()
car_manager = CarManager()



game_is_on = True
run = 1
while game_is_on:
    time.sleep(0.1)
    screen.update()


    if player.ycor() >= 280:
        scoreboard.update_score()
        player.reset_player()
        car_manager.increase_speed()


    if run % 6 == 0:
        car_manager.create_car()

    for car in car_manager.cars:
        if car.distance(player) <= 20:
            game_is_on = False
            # scoreboard.game_over()

    car_manager.move_cars()
    run += 1

scoreboard.game_over()
screen.exitonclick()
