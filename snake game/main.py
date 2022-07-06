from time import time
from turtle import Screen, Turtle, ycor
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = Scoreboard()


screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food)  < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.segments[0].xcor() < -300 or snake.segments[0].xcor() > 300 or snake.segments[0].ycor() < -300 or snake.segments[0].ycor() > 300:
        is_game_on = False
        score.game_over()
    
    
    for seg in snake.segments[1:]:
       
         if snake.segments[0].distance(seg) < 10:
            is_game_on = False
            score.game_over()




















screen.exitonclick()