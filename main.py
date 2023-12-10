from turtle import Turtle, Screen
from blocks import Block,blocks
from paddle import Paddle
from ball import Ball


screen = Screen()
# screen.tracer(0)

border_left = Turtle()
border_left.penup()
border_left.shape("square")
border_left.shapesize(30.5, 0.5)
border_left.goto(-300, 0)

border_right = Turtle()
border_right.penup()
border_right.shape("square")
border_right.shapesize(30.5, 0.5)
border_right.goto(300, 0)

border_up = Turtle()
border_up.penup()
border_up.shape("square")
border_up.shapesize(0.5, 30.5)
border_up.goto(0, 300)

border_down = Turtle()
border_down.penup()
border_down.shape("square")
border_down.shapesize(0.5, 30.5)
border_down.setpos(0, -300)


paddle = Paddle()
block_obj = Block()
ball = Ball()
 



pause = False
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

# for _ in range(300):
while blocks != []:
    ball.fd(10)
    # print(ball.pos())
    for block in blocks:
        # print(block.pos())
        if(abs(ball.xcor()-block.xcor())<20 and abs(ball.ycor()-block.ycor())<20):
            if(abs(ball.xcor()-block.xcor()) > abs(ball.ycor()-block.ycor())):
                ball.setheading(180-ball.heading())
            else:
                ball.setheading(-ball.heading())
            blocks.remove(block)
            block.hideturtle()
            break
            # block.color("blue")


    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.setheading(-ball.heading())

    if ball.xcor() > 280 or ball.xcor() < -280:
        ball.setheading(180-ball.heading())

    # screen.update()
    
    if(abs(ball.xcor()-paddle.xcor())<50 and abs(ball.ycor()-paddle.ycor())<20):
        ball.setheading(abs(ball.towards(paddle)-ball.heading()))

print(screen)



# print(blocks)

# for block in blocks:
#     if paddle.distance(block) < 20:
#         print("hit")
#         block.hideturtle()
#         blocks.remove(block)
#         ball.bounce_y()
#         ball.bounce_x()

# while(screen):
#     screen.exitonclick()
#     print(1)

screen.screensize(600, 600)

screen.exitonclick()
