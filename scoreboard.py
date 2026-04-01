from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.high_score = 0
        self.goto(0, 260)
        self.write_score()


    def add_point(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_board(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.write_score()