from turtle import Turtle
import random
from paddle_drawers import X_SIZE, Y_SIZE
import time


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.score = [0, 0]

    def ball_start(self):
        self.home()
        for i in range(3):
            self.write(arg=3 - i, font=("Verdana", 20, "bold"))
            time.sleep((i + 1) / (i + 1))
            self.clear()
        self.setheading(random.choice((random.randint(-45, 45), random.randint(135, 225))))

    def move(self, score_left=0, score_right=0):
        if self.position()[0] < 0:
            self.forward(7 + 1 * score_left)
        else:
            self.forward(7 + 1 * score_right)

    def bounce(self, left_paddle, right_paddle):
        if abs(self.position()[1]) >= Y_SIZE/2 - 20:
            self.setheading(-self.heading())
        if abs(self.position()[0]) >= X_SIZE/2 - 60 and (self.distance(left_paddle) <= 51 or self.distance(right_paddle) <= 51):
            self.setheading(180 - self.heading())
        elif abs(self.position()[0]) >= X_SIZE/2 + 250:
            if self.position()[0] < 0:
                self.score[1] += 1
                self.clear()
                self.ball_start()
            elif self.position()[0] > 0:
                self.score[0] += 1
                self.clear()
                self.ball_start()
