from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto((0, 0))
        self.x_dir = 10
        self.y_dir = 10
        self.move_speed = 0.1

    def set_direction(self):
        heading = random.randint(0, 360)
        self.setheading(heading)

    def move(self):
        new_x = self.xcor() + self.x_dir
        new_y = self.ycor() + self.y_dir
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_dir *= -1
        self.move_speed *= 0.9

    def bounce_y(self):
        self.y_dir *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto((0, 0))
        self.bounce_x()
        self.move_speed = 0.1
