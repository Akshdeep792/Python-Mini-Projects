from turtle import Screen, Turtle
import random
import turtle

flash = Turtle()
turtle.colormode(255)
flash.shape("turtle")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

directions = [0, 90, 180, 270]
flash.pensize(15)
flash.speed("fastest")

for _ in range(200):
    flash.color(random_color())
    flash.forward(30)
    flash.setheading(random.choice(directions))