from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,xc,yc):
        super().__init__()
        self.shape("square")
        self.shapesize(5,1)
        self.color("White")
        self.penup()
        self.goto(xc,yc)
        self.speed("fastest")

    def go_up(self):
        newy= self.ycor()+40
        self.goto(self.xcor(), newy)

    def go_down(self):
        newy= self.ycor()-40
        self.goto(self.xcor(), newy)