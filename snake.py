import time
from turtle import Screen, Turtle

STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    body = []

    def __init__(self):
        self.make_snake()
        self.head = self.body[0]

    def make_square(self, position):
        snake_part = Turtle(shape="circle")
        snake_part.fillcolor("green")
        snake_part.penup()
        snake_part.goto(position)
        self.body.append(snake_part)

    def make_snake(self):
        for position in STARTING_POSITIONS:
            self.make_square(position)

    def move(self):
        for segment_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[segment_num - 1].xcor()
            new_y = self.body[segment_num - 1].ycor()
            self.body[segment_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self):
        self.make_square(self.body[-1].position())

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)