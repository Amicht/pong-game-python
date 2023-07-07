from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.goto(0, 200)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.l_score} : {self.r_score}", align="center", font=("Courier", 30, "normal"))

    def l_player_point(self):
        self.l_score += 1
        self.update_score()

    def r_player_point(self):
        self.r_score += 1
        self.update_score()