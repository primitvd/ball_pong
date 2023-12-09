from turtle import Turtle, Screen
from blocks import Block,blocks
from paddle import Paddle
from ball import Ball


# border_left = Turtle()
# border_left.penup()
# border_left.shape("square")
# border_left.shapesize(30.5, 0.5)
# border_left.goto(-300, 0)

# border_right = Turtle()
# border_right.penup()
# border_right.shape("square")
# border_right.shapesize(30.5, 0.5)
# border_right.goto(300, 0)

# border_up = Turtle()
# border_up.penup()
# border_up.shape("square")
# border_up.shapesize(0.5, 30.5)
# border_up.goto(0, 300)

# border_down = Turtle()
# border_down.penup()
# border_down.shape("square")
# border_down.shapesize(0.5, 30.5)
# border_down.setpos(0, -300)


paddle = Paddle()
# block = Block()
ball = Ball()
 

screen = Screen()


pause = True
def play():
    global pause
    if pause == True:
        pause = False
    else:
        pause = True
    
screen.onkey(play(), key = "space")
screen.onkeypress(paddle.move_left, "Left")
screen.onkeypress(paddle.move_right, "Right")
screen.listen()

while pause:
    ball.fd(1)



print(screen)

while(screen):
    screen.exitonclick()
    print(1)

screen.screensize(600, 600)

screen.exitonclick()
