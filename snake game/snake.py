from turtle import Turtle

position = [(0, 0), (-20, 0) , (-40, 0)]
move_dist = 20
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
    
    def create_snake(self):
        for pos in position:
           self.add_segment(pos)
        
    def add_segment(self, position):
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            snake.goto(position)
            self.segments.append(snake)

    def extend(self):
            self.add_segment(self.segments[-1].position())
    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg  - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(move_dist)
    
    def up(self):
        self.segments[0].setheading(90)
    
    def down(self):
        self.segments[0].setheading(270)

    def left(self):
        self.segments[0].setheading(180)
    
    def right(self):
        self.segments[0].setheading(0)