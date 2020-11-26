# Todo 1: Classes are paddle, ball, score.
# Todo 2: Tasks are class creation, procedures of hitting walls and bounce
# Todo 3: Another tasks are procedures of missing walls and score increase

from turtle import Screen
from paddle_drawers import Paddle, Drawer, X_SIZE, Y_SIZE
from ball import Ball
import time


# Preparation of the scene.
playground = Screen()
playground.bgcolor("black")
playground.setup(width=X_SIZE, height=Y_SIZE)
playground.title("A game of Pong")

right = Paddle(position="right")
left = Paddle(position="left")

upper_drawer = Drawer("up")
bottom_drawer = Drawer("down")
announcer = Drawer(direction="center")
announcer.write(arg="The ball will be sent out randomly.\n"
                "Whoever scores 25 points wins.\n"
                "The more points you score,\n"
                "the faster ball runs on your side of the field.", font=("Verdana", 18, "bold"))
time.sleep(2)
playground.listen()
playground.onkey(fun=right.go_up, key="Up")
playground.onkey(fun=right.go_down, key="Down")
playground.onkey(fun=left.go_up, key="w")
playground.onkey(fun=left.go_down, key="s")

counter = 0
bouncey = Ball()
bouncey.ball_start()
announcer.clear()
playground.tracer(0)
game_continues = True
while game_continues:
    upper_drawer.score = bouncey.score[0]
    bottom_drawer.score = bouncey.score[1]
    upper_drawer.display_score(upper_drawer.score)
    bottom_drawer.display_score(bottom_drawer.score)
    playground.update()
    bouncey.move(score_left=bouncey.score[0], score_right=bouncey.score[1])
    bouncey.bounce(left, right)
    playground.update()
    time.sleep(0.01)
    if upper_drawer.score >= 25 or bottom_drawer.score >= 25:
        game_continues = False

announcer.write(arg="The game is over as 25 balls were missed", font=("Verdana", 25, "bold"))


playground.exitonclick()
