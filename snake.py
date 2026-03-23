from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create()
        self.head = self.segments[0]


    def create(self):
        for position in STARTING_POSITIONS:
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    def move(self) -> None:
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)

        self.head.forward(MOVE_DISTANCE)

    def turn_left(self):
        self.head.setheading(180)

    def turn_right(self):
        self.head.setheading(0)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)
