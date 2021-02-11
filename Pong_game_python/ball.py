from turtle import Turtle

class Ball(Turtle):
    def __init__(self,xc,yc):
        super().__init__()
        self.shape("circle")
        # self.shapesize(5,1)
        self.color("Yellow")
        self.penup()
        self.goto(xc,yc)
        self.move_speed = 0.05
        self.xmove =10
        self.ymove= 10

    def move(self):
        newx= self.xcor() + self.xmove
        newy= self.ycor() + self.ymove
        self.goto(newx,newy)

    def bounce_y(self):
        self.ymove *= -1 

    def bounce_x(self):
        self.xmove *= -1 
        self.move_speed *= 0.9

    def reset_ball(self):
        self.goto(0,0)  
        self.bounce_x()  
        self.move_speed= 0.05