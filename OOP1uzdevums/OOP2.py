from turtle import *
tdraw = Turtle()

class Kvadrats:
    def __init__(self, nosaukums):
        self.nosaukums = nosaukums

    def drawSquare(self):
        tdraw.up()
        tdraw.pensize(4)
        tdraw.goto(-200, 200)
        tdraw.down()
        tdraw.fillcolor("red")
        tdraw.begin_fill()
        tdraw.fd(200)
        tdraw.rt(90)
        tdraw.fd(200)
        tdraw.rt(90)
        tdraw.fd(200)
        tdraw.rt(90)
        tdraw.fd(200)
        tdraw.end_fill()


class Tainssturis:
    def __init__(self, nosaukums):
        self.nosaukums = nosaukums

        
    def drawRectangle(self):
        tdraw.up()
        tdraw.pensize(4)
        tdraw.goto(200, -200)
        tdraw.down()
        tdraw.fillcolor("blue")
        tdraw.begin_fill()
        tdraw.fd(300)
        tdraw.rt(90)
        tdraw.fd(100)
        tdraw.rt(90)
        tdraw.fd(300)
        tdraw.rt(90)
        tdraw.fd(100)
        tdraw.end_fill()


class Trijsturis:
    def __init__(self, nosaukums):
        self.nosaukums = nosaukums
        
    def drawTriangle(self):
        tdraw.up()
        tdraw.pensize(4)
        tdraw.goto(-100, -220)
        tdraw.down()
        tdraw.fillcolor("yellow")
        tdraw.begin_fill()
        tdraw.fd(200)
        tdraw.rt(120)
        tdraw.fd(200)
        tdraw.rt(120)
        tdraw.fd(200)
        tdraw.rt(120)
        tdraw.end_fill()




