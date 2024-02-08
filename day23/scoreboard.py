from turtle import Turtle, write
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-220, 260)
        self.write_score()

    def update_score(self):
        self.level += 1
        self.write_score()
        
    def write_score(self):
        self.clear()
        self.write(f'Level: {self.level}', align='center', font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write('Game Over', align='center', font=FONT)
