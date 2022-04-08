from turtle import *
tdraw = Turtle()

class Geo:
    def __init__(self, color, tips):
        self.color = color
        self.tips = tips
        self.pensize = 4

    def drawSquare(self):
        tdraw.up()
        tdraw.pensize(self.pensize)
        tdraw.goto(-100, 200)
        tdraw.down()
        tdraw.fillcolor(self.color)
        tdraw.begin_fill()
        tdraw.fd(200)
        tdraw.rt(90)
        tdraw.fd(200)
        tdraw.rt(90)
        tdraw.fd(200)
        tdraw.rt(90)
        tdraw.fd(200)
        tdraw.end_fill()

    def drawRectangle(self):
        tdraw.up()
        tdraw.pensize(self.pensize)
        tdraw.goto(30, -200)
        tdraw.down()
        tdraw.fillcolor(self.color)
        tdraw.begin_fill()
        tdraw.fd(100)
        tdraw.rt(90)
        tdraw.fd(300)
        tdraw.rt(90)
        tdraw.fd(100)
        tdraw.rt(90)
        tdraw.fd(300)
        tdraw.end_fill()
    
    def drawTriangle(self):
        tdraw.up()
        tdraw.pensize(self.pensize)
        tdraw.goto(-100, -220)
        tdraw.down()
        tdraw.fillcolor(self.color)
        tdraw.begin_fill()
        tdraw.fd(200)
        tdraw.rt(120)
        tdraw.fd(200)
        tdraw.rt(120)
        tdraw.fd(200)
        tdraw.rt(120)
        tdraw.end_fill()



    def draw(self):
        if self.tips == "square":
            self.drawSquare()
        elif self.tips == "rectangle":
            self.drawRectangle()
        elif self.tips == "triangle":
            self.drawTriangle()
    
        
p1 = Geo("red", "square")

p2 = Geo("blue", "rectangle")

p3 = Geo("Yellow", "triangle")

visi = [p1,p2,p3]
for x in visi:
    x.draw()
