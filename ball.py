from turtle import Turtle

MOVE_SIZE = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = MOVE_SIZE
        self.y_move = MOVE_SIZE
        self.move_speed = 0.1
        self.color("white")
        self.shape("circle")
        self.penup()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.move_speed *= 0.9
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def reset_position(self):
        self.move_speed = 0.1
        self.goto(0, 0)
        self.bounce_x()


