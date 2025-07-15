from turtle import Turtle, Screen
from snake import Snake
from food import Food
from snakeboard import Snakeboard
import time

screen = Screen()


screen.setup(height = 600, width = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
snakeboard = Snakeboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    #detect the collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        snakeboard.increase_score()
    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 or snake.head.xcor() < -280:
        game_is_on = False
        snakeboard.game_over()

    #detect collision with tail
    for segment in snake.segments[1:]:
        # if head collides with any segments in a tail that this means :
        # trigger game_over
        if snake.head.distance(segment) < 10:
            game_is_on = False
            snakeboard.game_over()
screen.exitonclick()

