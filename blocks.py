from turtle import Turtle
import random

block_size = 0.7
block_size_increment = int(block_size * 10)
blocks = []

class Block(Turtle):

    def __init__(self):
        super().__init__()
        self.speed(0)
        self.penup()
        self.hideturtle()
        self.shape("square")
        self.shapesize(block_size,block_size)
        self.shapesize(block_size,block_size)
        for x in range(250*10,100*10,-block_size_increment*25):
            for y in range(-250*10,250*10,block_size_increment*25):
                self.goto(y/10,x/10)
                self.showturtle()
                # blocks.append(self.clone())
                if random.randint(0,1) == 1:
                    self.showturtle()
                    blocks.append(self.clone())
                else:
                    self.hideturtle()
        self.hideturtle()


