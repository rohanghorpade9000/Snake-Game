import turtle
from turtle import Turtle

with open("data.txt") as file:
    contents = int(file.read())

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = contents
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0,260)
        self.write(f"Score : {self.score}", False, "Center", ("Arial", 16, "normal"))
        self.update_scoreboard()


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode='w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} Highscore : {self.high_score}", False, "Center", ("Arial", 16, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()







