import turtle
class Disk(object):
    def __init__(self, name="",xpos=0,ypos=0,height=20,width=40):
        self.dname=name
        self.dxpos=xpos
        self.dypos=ypos
        self.dheight=height
        self.dwidth=width

    def showdisk(self):
        turtle.setheading(90)
        turtle.forward(self.dwidth/2)
        turtle.left(90)
        turtle.forward(self.dheight)
        turtle.left(90)
        turtle.forward(self.dwidth)
        turtle.left(90)
        turtle.forward(self.dheight)
        turtle.left(90)
        turtle.forward(self.dwidth/2)

    def newpos(self,xpos,ypos):
        turtle.penup()
        turtle.setpos(xpos,ypos)
        turtle.pendown()
        
    def cleardisk(self):
        turtle.pencolor("white")
        turtle.setheading(90)
        turtle.forward(self.dwidth/2)
        turtle.left(90)
        turtle.forward(self.dheight)
        turtle.left(90)
        turtle.forward(self.dwidth)
        turtle.left(90)
        turtle.forward(self.dheight)
        turtle.left(90)
        turtle.forward(self.dwidth/2)
        turtle.pencolor("black")