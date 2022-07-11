from tkinter import CENTER
from turtle import Turtle

with open(r"./snake game/highscore.txt") as file:
                content  = file.read()
                
                file.close()
class Scoreboard(Turtle):

    def __init__(self) :
        super().__init__()
        self.score = 0
        self.highscore = int(content)
        self.color("white")
        self.penup()
        self.goto(0, 268)
        self.hideturtle()
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=("Arial", 24, "normal") )
    
    def reset(self):
        if self.score > self.highscore: 
            with open(r"./snake game/highscore.txt", mode="w") as file:
                file.write(str(self.score))
            # self.highscore = self.score
            with open(r"./snake game/highscore.txt") as file:
                content  = file.read()
                self.highscore = int(content)
                file.close()
        self.score = 0
        self.update_score()
    
    def increase_score(self):
        self.score+=1       
        self.update_score()

