import pygame as py
import random as rd

SIZE = (1000,1000)
TITLE = "RandomPaintingGenerator"
POINTS_NUMBER = 10000

py.init()
gameDisplay = py.display.set_mode(SIZE)
py.display.set_caption(TITLE)

class Point:
    def __init__(self,size,pos,color):
        self.size = size
        self.pos = pos
        self.color = color

class PointFactory:
    def __init__(self,sizeRange):
        self.sizeRange = sizeRange
        self.posRange = SIZE

    def CreatePoint(self):
        size = rd.randrange(self.sizeRange[0],self.sizeRange[1])
        pos = (rd.randint(0,self.posRange[0]),rd.randint(0,self.posRange[1]))
        color = (rd.randint(0,255),rd.randint(0,255),rd.randint(0,255))
        return Point(size,pos,color)


if __name__ == "__main__":

    quit = False
    pointFactory = PointFactory((2,20))
    points =[]
    for i in range(POINTS_NUMBER):
        points.append(pointFactory.CreatePoint())

    for point in points:
        py.draw.circle(gameDisplay,point.color,point.pos,point.size,rd.randrange(0,point.size))

    while not quit:

        for event in py.event.get():
            if event.type == py.QUIT:
                quit = True

        py.display.update()