from turtle import Turtle
import random 

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self) -> None:
        self.cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        t = Turtle()
        t.penup()
        t.color(random.choice(COLORS))
        t.shape('square')
        t.shapesize(stretch_wid=1, stretch_len=2)
        t.setheading(180)
        t.goto(300, random.randint(-250, 250))
        self.cars.append(t) 
        
    
    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT

    def move_cars(self):
        for car in self.cars:
            car.forward(self.move_speed)

