from turtle import Screen, Turtle
screen = Screen()

def create_screen() -> None:
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Arcade Game")

def init_body() -> None:
    starting_positions = [(0, 0), (-20, 0), (-40, 0)]

    for position in starting_positions:
        segment = Turtle(shape="square")
        segment.color("white")
        segment.goto(position)

if __name__ == "__main__":
    create_screen()
    init_body()
    screen.exitonclick()

