from turtle import Turtle

starting_posx=[(-40,0),(-20,0),(0,0)]
move_distance=20

UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def create_snake(self):
        for position in starting_posx:
            self.add_segment(position)
            
    def __init__(self, snakecolor):
        self.segments=[]
        self.snake_color= snakecolor
        self.create_snake()
        self.head = self.segments[0]
        
        
    
    def move(self):
        for seg_no in range(len(self.segments)-1,0,-1):
            newx= self.segments[seg_no -1].xcor()
            newy= self.segments[seg_no -1].ycor()
            self.segments[seg_no].goto(newx, newy)
        self.head.forward(move_distance)    

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        new_t = Turtle(shape="square")
        new_t.color(self.snake_color)
        new_t.penup()
        new_t.speed(0)
        new_t.goto(position)
        self.segments.append(new_t)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
