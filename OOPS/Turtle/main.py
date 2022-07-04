from turtle import Screen, Turtle

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

flash = Turtle()
flash.shape("turtle")
flash.pensize(5)

x = 3
i = 0
while not x==11:
    angle = int(360/x)
    flash.color(colours[i])
    for i in range(x):
        flash.forward(100)
        flash.left(angle)
    x = x+1
    i = i+1

    

screen = Screen()
screen.exitonclick()
