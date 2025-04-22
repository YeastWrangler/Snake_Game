from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.setpos(0,260)
        self.color("white")
        self.hideturtle()
        self.update_score()
        self.penup()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setpos(0,0)
        self.color("red")
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)