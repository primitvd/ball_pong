from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.speed(0)
        self.penup()
        self.hideturtle()
        self.shape("square")
        self.goto(0,-250)
        self.showturtle()
        for x in range(1,50,1):
            self.shapesize(1,x/10.0)
        self.shapesize(1,5)

    def move_left(self):
        if self.xcor() > -240:
            self.setx(self.xcor() - 20)

    def move_right(self):
        if self.xcor() < 240:
            self.setx(self.xcor() + 20)