from turtle import Turtle

FONT = ('Arial', 15, 'normal')
ALIGNMENT = 'center'

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.highscore = self.read_highscore()
        self.score = 0
        self.hideturtle()
        self.color('white')
        self.pencolor('white')
        self.speed('fastest')
        self.penup()
        self.goto(0, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        text = f'Score: {self.score} High score: {self.highscore}'
        self.clear()
        self.write(text, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def read_highscore(self):
        with open('data.txt') as file:
            hs = int(file.read())
            return hs


    def update_highscore(self, hs):
        with open('data.txt', mode='w') as file:
            file.write(str(hs))


    
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write('GAME OVER', align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.update_highscore(self.highscore)
        self.score = 0
        self.update_scoreboard()
