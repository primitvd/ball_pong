from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.speed(0)
        self.penup()
        self.hideturtle()
        self.shape("circle")
        self.shapesize(0.7,0.7)
        self.goto(0,-232)
        self.showturtle()
        self.setheading(85)