from turtle import Turtle
FONT = ("arial", 22, "normal")
ALIGN = "center"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        with open("/users/mohamed arous/Desktop/data.txt", mode="r") as f:
            self.high_score = int(f.read())
        self.update_scoreboard()
        self.hideturtle()


    def update_scoreboard(self):
        self.clear()
        self.write(f"score: {self.score} , high score : {self.high_score}", align=ALIGN, font=FONT)


    def reset(self):
        if self.score > self.high_score :
             self.high_score = self.score
             with open("/users/mohamed arous/Desktop/data.txt", mode="w") as f:
                 f.write(f"{self.high_score}")


        self.score = 0
        self.update_scoreboard()

    #def game_over(self):
       # self.goto(0,0)
       # self.write("game over",align= ALIGN,font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
