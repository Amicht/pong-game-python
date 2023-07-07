from turtle import Turtle

START_POSITIONS = [()]
MOVE_SIZE = 30

class Racket(Turtle):

    def __init__(self, position, half_screen_height):
        super().__init__()
        self.top_limit = half_screen_height - 50
        self.bottom_limit = half_screen_height * -1 + 50
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)
        self.goto(position)

    def up(self):
        if self.ycor() + MOVE_SIZE > self.top_limit:
            return
        self.setposition(self.xcor(), self.ycor() + MOVE_SIZE)

    def down(self):
        if self.ycor() - MOVE_SIZE < self.bottom_limit:
            return
        self.setposition(self.xcor(), self.ycor() - MOVE_SIZE)