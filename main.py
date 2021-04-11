import turtle
from random import randint
from data import *
from math import sqrt, atan2
from random import randint, choice

def setup_screen(screen: turtle.Screen) -> None:
    screen.bgcolor("black")
    screen.title("Pong")
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.onkeypress(lambda: p1.sety(p1.ycor() + MOVE_UP), "Up")
    screen.onkeypress(lambda: p1.sety(p1.ycor() - MOVE_DOWN), "Down")
    screen.onkeypress(lambda: p2.sety(p2.ycor() + MOVE_UP), "w")
    screen.onkeypress(lambda: p2.sety(p2.ycor() - MOVE_DOWN), "s")
    screen.listen()
    screen.tracer(0)

def setup_players() -> None:
    p1.penup()
    p2.penup()
    p1.color("white")
    p1.shapesize(7,1)
    p2.color("white")
    p2.shapesize(7,1)
    p1.setpos(SCREEN_WIDTH / 2 - 20, 0)
    p2.setpos(-SCREEN_WIDTH / 2 + 20, 0)
    ball.penup()

def setup_scoreboard() -> None:
    score_board.penup()
    score_board.setpos(-10, SCREEN_HEIGHT / 2 - 40)
    score_board.color("white")
    score_board.write(f"{score_p2}:{score_p1}", move=False, align="center", font=("Arial", 30, "normal"))
    score_board.hideturtle()

def layout_setup(screen: turtle.Turtle) -> None:
    setup_screen(screen)
    setup_players()
    setup_scoreboard()

def handle_ball_bounds() -> None:
    global score_p1, score_p2, BALL_DY
    if ball.xcor() > SCREEN_WIDTH / 2 - 20: 
        score_p2 += 1
        set_state()
    elif ball.xcor() < -SCREEN_WIDTH / 2 + 20: 
        score_p1 += 1
        set_state()
    elif ball.ycor() >= SCREEN_HEIGHT / 2 or ball.ycor() <= -SCREEN_HEIGHT / 2:
        BALL_DY *= -1

def move_ball() -> None:
    global BALL_X, BALL_DX, BALL_DIRECTION, BALL_Y, BALL_DY
    BALL_DX += 0.1 * BALL_DIRECTION
    BALL_DY += 0.1 * BALL_DIRECTION
    BALL_X += BALL_DX / 60
    BALL_Y += BALL_DY / 60
    ball.setpos(BALL_X, BALL_Y)
    turtle.update()

def check_collision(player: turtle.Turtle) -> bool:
    return int(sqrt(pow(player.xcor() - ball.xcor(), 2) + pow(player.ycor() - ball.ycor(), 2))) < 60

def set_state() -> None:
    global BALL_X, BALL_Y, BALL_DX, BALL_DY, BALL_DIRECTION
    BALL_DIRECTION = choice((-1, 1))
    BALL_DX, BALL_DY = 0, 0
    BALL_X, BALL_Y = 0, 0
    score_board.clear()
    score_board.write(f"{score_p2}:{score_p1}", move=False, align="center", font=("Arial", 30, "normal"))
    ball.setpos(BALL_X, BALL_Y)
    p1.setpos(SCREEN_WIDTH / 2 - 20, 0)
    p2.setpos(-SCREEN_WIDTH / 2 + 20, 0)

if __name__ == "__main__":
    screen = turtle.Screen()
    layout_setup(screen)
    while True:
        screen.update()
        if check_collision(p1) or check_collision(p2):
            BALL_DX *= -1
            BALL_DY *= -1
            BALL_DIRECTION *= -1
            screen.update()
        move_ball()
        handle_ball_bounds()