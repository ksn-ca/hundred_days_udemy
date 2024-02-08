from snake import Snake
from food import Food
from turtle import Screen, Turtle
import time
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snek geme")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # collisiton
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # collision
    snake_head_x = snake.head.xcor()
    snake_head_y = snake.head.ycor()
    if (
        snake_head_x > 290
        or snake_head_x < -290
        or snake_head_y > 290
        or snake_head_y < -290
    ):
        # game_is_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
