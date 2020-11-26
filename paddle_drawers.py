from turtle import Turtle

X_SIZE = 1200
Y_SIZE = 600


class Paddle(Turtle):
    def __init__(self, position):
        super(Paddle, self).__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.penup()
        if position == "right":
            self.setposition(x=X_SIZE/2 - 50, y=0)
            self.setheading(90)
        else:
            self.setposition(x=-X_SIZE/2 + 50, y=0)
            self.setheading(90)

    def go_up(self):
        if self.position()[1] < Y_SIZE/2 - 30:
            self.forward(40)

    def go_down(self):
        if self.position()[1] > -Y_SIZE/2 + 30:
            self.backward(40)


class Drawer(Turtle):
    def __init__(self, direction):
        super(Drawer, self).__init__()
        self.hideturtle()
        self.color("white")
        self.score = 0
        if direction == "up":
            self.setheading(90)
            while self.position()[1] <= Y_SIZE/2:
                self.forward(10)
                self.penup()
                self.forward(10)
                self.pendown()
            self.penup()
            self.setposition(-150, self.position()[1] - 80)
        elif direction == "down":
            self.setheading(270)
            while self.position()[1] >= -Y_SIZE/2:
                self.forward(10)
                self.penup()
                self.forward(10)
                self.pendown()
            self.penup()
            self.setposition(105, -self.position()[1] - 80)
        else:
            self.penup()
            self.setposition(x=-375, y=0)

    def display_score(self, score=0):
        self.clear()
        self.write(arg=score, font=("Verdana", 25, "bold"))


