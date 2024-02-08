from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.color("green")
        self.setheading(90)

    def move(self):
        if self.ycor() < FINISH_LINE_Y:
            self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def reset_player(self):
        self.goto(STARTING_POSITION)
