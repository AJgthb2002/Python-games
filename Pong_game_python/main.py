from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen= Screen()
screen.bgcolor("dark slate blue")
screen.setup(800, 600)
screen.title("AJ's Pong")
screen.tracer(0)

middle= Turtle()
middle.left(90)
for _ in range(80):
    middle.forward(10)
    middle.penup()
    middle.forward(10)
    middle.pendown()
middle.penup()
middle.goto(0,0)
middle.setheading(270)
for _ in range(80):
    middle.forward(10)
    middle.penup()
    middle.forward(10)
    middle.pendown()
middle.hideturtle()

paddleright= Paddle(360,0)
paddleleft= Paddle(-360,0)
ball= Ball(0,0)
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(paddleright.go_up, "p")
screen.onkeypress(paddleright.go_down, "l")
screen.onkeypress(paddleleft.go_up, "q")
screen.onkeypress(paddleleft.go_down, "a")

game_on= True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()


    # detect paddle miss
    if ball.xcor()> 360: 
        ball.reset_ball()
        scoreboard.l_point()

    if ball.xcor() < -360:
        ball.reset_ball()    
        scoreboard.r_point()

    #detect collision with paddles
    if (ball.distance(paddleright) < 50 and ball.xcor()> 330) or (ball.distance(paddleleft) < 50 and ball.xcor()< -330):
        ball.bounce_x()  

    

screen.exitonclick()