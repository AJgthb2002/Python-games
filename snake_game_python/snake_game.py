from turtle import *
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

#setting up the screen
screen= Screen()
screen.setup(600,600)
bgpic(picname= "C:\Data\Ananya\python files\\100daysofcode_angelaYuCourse\\turtle-project- day19\snake game\images\\soil.png")
# screen.bgcolor("black")
screen.title("AJ's Snake Game")
screen.tracer(0)

snake_color = screen.textinput("Welcome to the classic Snake game!", "Choose the color of your snake (Gold/White/Lime)")
if snake_color in ["gold","lime","white"]:
    snake= Snake(snake_color)
else:
    snake= Snake("lime")    
apple1= Food()
apple2= Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right,"Right")
screen.update()

game_on=True

while game_on:
   
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # detect collision with apples
    if snake.head.distance(apple1) < 18:
        apple1.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.distance(apple2) < 18:
        apple2.refresh()
        snake.extend()
        scoreboard.increase_score()    

    # detect collision with walls
    if snake.head.xcor()>=295 or snake.head.xcor()<= -295 or snake.head.ycor()>=295 or snake.head.ycor()<= -295:
        game_on=False
        scoreboard.game_over()

    # detect collision with tail
    for seg in range(2,len(snake.segments)-1):
        if seg == 0 or seg==1:
            pass
        elif snake.head.distance(snake.segments[seg]) < 10:
            game_on=False
            scoreboard.game_over()

screen.exitonclick()