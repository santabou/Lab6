import turtle
from Disk import Disk

class Pole(object):
    def __init__(self, name="", xpos=0, ypos=0, thick=10, length=100):
        self.pname = name
        self.stack = []
        self.toppos = 0
        self.pxpos = xpos
        self.pypos = ypos
        self.pthick = thick
        self.plength = length

    def showpole(self):
        turtle.penup()
        turtle.goto(self.pxpos, self.pypos)
        turtle.pendown()

        turtle.forward(self.pthick/2)
        turtle.left(90)
        turtle.forward(self.plength)
        turtle.left(90)
        turtle.forward(self.pthick)
        turtle.left(90)
        turtle.forward(self.plength)
        turtle.left(90)
        turtle.forward(self.pthick/2)

    def pushdisk(self, Disk):
        Disk.newpos(self.pxpos, self.toppos)
        Disk.showdisk()

        self.toppos += Disk.dheight
        self.stack.append(Disk)

    def popdisk(self):
        outputdisk = self.stack.pop()
        self.toppos -= outputdisk.dheight

        outputdisk.newpos(self.pxpos, self.toppos)
        outputdisk.cleardisk()
        return outputdisk