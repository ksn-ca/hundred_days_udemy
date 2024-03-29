from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position): 
        super().__init__()
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.shape("square")
        self.goto(position)

    def up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        if self.ycor() > -250:
            self.goto(self.xcor(), self.ycor() - 20)
