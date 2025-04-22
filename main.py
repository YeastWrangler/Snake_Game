import time
from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard

def play_game():
    screen = Screen()
    GAME_HEIGHT = 600
    GAME_WIDTH = 600
    BOUNDARY = 290
    screen.setup(width=GAME_WIDTH, height=GAME_HEIGHT)
    screen.bgcolor("black")
    screen.title("Snake Game!")
    screen.tracer(0)
    game_on = True

    snake = Snake()
    food = Food()
    score = Scoreboard()
    screen.textinput("Ready?", "press enter to play")

    screen.listen()
    screen.onkey(key="Up", fun=snake.move_up)
    screen.onkey(key='Down', fun=snake.move_down)
    screen.onkey(key="Left", fun=snake.move_left)
    screen.onkey(key="Right", fun=snake.move_right)

    while game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 15:
            score.increase_score()
            snake.add_segment()
            food.refresh()
        if snake.head.xcor() > BOUNDARY or snake.head.xcor() < -BOUNDARY or snake.head.ycor() > BOUNDARY or snake.head.ycor() < -BOUNDARY:
            game_on = False
        for segment in snake.body[1:]:
            if snake.head.distance(segment) < 10:
                game_on = False


    score.game_over()
    screen.exitonclick()
play_game()
