from turtle import Screen, Turtle
import random
import turtle

flash = Turtle()
turtle.colormode(255)
flash.setheading(180)
flash.shape("turtle")
flash.speed("fastest")
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color


for i in range(361):
    flash.color(random_color())
    flash.circle(100)
    flash.left(1)