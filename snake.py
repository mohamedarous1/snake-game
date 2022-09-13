from turtle import Turtle
COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.tims = []
        self.create_snake()
        self.head = self.tims[0]
    def create_snake(self):
        for position in COORDINATES:
            self.add_snake(position)

    def add_snake(self,position):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.tims.append(tim)



    def reset(self):
        for tim in self.tims :
            tim.goto(1000,1000)

        self.tims.clear()
        self.create_snake()
        self.head = self.tims[0]



    def exend(self):
        self.add_snake(self.tims[-1].position())


    def move(self):
        for y in range(len(self.tims) - 1, 0, -1):
            new_x = self.tims[y - 1].xcor()
            new_y = self.tims[y - 1].ycor()
            self.tims[y].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)