#1. 创建游戏背景
import turtle as t
import random

mz = t.Screen()
mz.setup(700,700)
mz.bgcolor('black')
mz.title('麦叔迷宫')
mz.register_shape('wall.gif')
mz.register_shape('pr.gif')
mz.register_shape('pl.gif')
mz.register_shape('e.gif')
mz.register_shape('gold.gif')
mz.tracer(0)

levels = []
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXX   XXXXXX  XXXXXXXXXXX",
"XXXP XXXXXXX  XXXXXXXXXXX",
"XXX  XXXXXXX  XXXXXXXXXXX",
"XXX                  XXXX",
"XXXXXXX XXXX  XXXXX  XXXX",
"XXXXXXXGXXXX  XXXXXE  EXX",
"XXXXXXXXXXXX  XXXXX   XXX",
"XXXXXXXXXXXX  XXXXX    XX",
"XX                     XX",
"XXXX  XXXXXX  XXXX  GXXXX",
"XXXX  XXXXXX  XXXXXXXXXXX",
"XXXXE            XXXXXXXX",
"XXXXXXXXXXEXXXX  XXXXXXXX",
"XXXXXXXXXXXXXXX  XXXXXXXX",
"XXXXGXXXXXXXXXX  XXEXXXXX",
"XX               XXXXXXXX",
"XX   XXXXXXXXXXXXXXXXXXXX",
"XX   XXXXX              X",
"XX   XXXXXXXXXXXXX  XXXXX",
"XX     XXXXXXXXXXX  XXXXX",
"XX            XXXX      X",
"XXXX                    X",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]
levels.append(level_1)

class Enemy(t.Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.shape('e.gif')
        self.speed(0)
        self.penup()
        
    def move(self):
        self.turn()
        if self.fx == 'U':
            go_x = self.xcor()
            go_y = self.ycor() + 24
        elif self.fx == 'D':
            go_x = self.xcor()
            go_y = self.ycor() - 24
        elif self.fx == 'R':
            go_x = self.xcor() + 24
            go_y = self.ycor()
        elif self.fx == 'L':
            go_x = self.xcor() - 24
            go_y = self.ycor()
        self.goto(go_x, go_y)
        t.ontimer(self.move, random.randint(100,300))
    def turn(self):
        #跟随功能
        if self.distance(player) < 96:
            if self.xcor() < player.xcor():
                self.fx = 'R'
            elif self.xcor() > player.xcor():
                self.fx = 'L'
            elif self.ycor() > player.ycor():
                self.fx = 'D'
            elif self.ycor() < player.ycor():
                self.fx = 'U'        
        else:
            self.fx = random.choice(['U', 'D', 'R', 'L'])
        
        
class Gold(t.Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.shape('gold.gif')
        self.speed(0)
        self.penup()
        
class Player(t.Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.shape('pr.gif')
        self.speed(0)
        self.penup()
    def go_right(self):
        go_x = self.xcor()+24
        go_y = self.ycor()
        self.shape('pr.gif')
        self.move(go_x, go_y)
    def go_left(self):
        go_x = self.xcor()-24
        go_y = self.ycor()
        self.shape('pl.gif')
        self.move(go_x, go_y)
    def go_up(self):
        go_x = self.xcor()
        go_y = self.ycor()+24
        self.move(go_x, go_y)        
    def go_down(self):
        go_x = self.xcor()
        go_y = self.ycor()-24
        self.move(go_x, go_y)
    def move(self, go_x, go_y):
        if (go_x, go_y) not in walls:
            self.goto(go_x, go_y)
            self.look_for_gold(go_x, go_y)
        else:
            print('哎呀，hitting wall')
    def look_for_gold(self, go_x, go_y):
        global score
        for g in golds:
            if g.distance(player) == 0:
                score += 1
                print(f"current score is {score}")
                g.ht()
                golds.remove(g)

class Pen(t.Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.shape('wall.gif')
        self.speed(0)
        self.penup()
    def make_maze(self, level):
        for i in range(len(level)):
            row = level[i]
            for j in range(len(row)):
                screen_x = -288 + 24 * j
                screen_y = 288 - 24 * i
                char = row[j]
                if char == 'X':
                    self.goto(screen_x, screen_y)
                    self.stamp()
                    walls.append((screen_x, screen_y)) #tuple
                elif char == 'P':
                    player.goto(screen_x, screen_y)
                    player.st()
                elif char == 'G':
                    gold = Gold()
                    golds.append(gold)
                    gold.goto(screen_x, screen_y)
                    gold.st()
                elif char == 'E':
                    ene = Enemy()
                    enemies.append(ene)
                    ene.goto(screen_x, screen_y)
                    ene.st()

score = 0
pen = Pen()
player = Player()
walls = []
golds = []
enemies = []
pen.make_maze(levels[0])

mz.listen()
mz.onkey(player.go_right, 'Right')
mz.onkey(player.go_left, 'Left')
mz.onkey(player.go_up, 'Up')
mz.onkey(player.go_down, 'Down')

for e in enemies:
    t.ontimer(e.move, random.randint(100,300))

while True:
    mz.update()

mz.mainloop()