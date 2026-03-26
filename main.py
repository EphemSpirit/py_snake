from turtle import Screen
from snake import Snake
from food import Food
import time
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Arcade Game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.turn_left, key="Left")
screen.onkey(fun=snake.turn_right, key="Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()

