from graphics import *

def drawLine(win, Pos1, Pos2, colour):
    line = Line(Pos1, Pos2)
    line.setFill(colour)
    line.draw(win)


def drawCircle(win, center, rad, colour):
    circ = Circle(center, rad)
    circ.setFill(colour)
    circ.draw(win)


def drawTriangle(win, point1, point2, point3, colour):
    triangle = Polygon(point1, point2, point3)
    triangle.setFill(colour)
    triangle.draw(win)

def drawFinalPatch(win, xCoord, yCoord, colour):

    topX1 = xCoord
    topY1 = yCoord
    topX2 = xCoord + 100
    topY2 = yCoord + 10

    bottomX1 = xCoord
    bottomY1 = yCoord
    bottomX2 = xCoord + 10
    bottomY2 = yCoord + 100

    for i in range(0, 100, 10):

        topPos1 = Point(topX1, topY1)
        topPos2 = Point(topX2, topY2)

        bottomPos1 = Point(bottomX1, bottomY1)
        bottomPos2 = Point(bottomX2, bottomY2)

        drawLine(win, topPos1, topPos2, colour)
        drawLine(win, bottomPos1, bottomPos2, colour)

        topX1 = topX1 + 10
        topY2 = topY2 + 10
        bottomX2 = bottomX2 + 10
        bottomY1 = bottomY1 + 10

    win.getMouse()


def drawPenultimatePatch(win, xCoord, yCoord, colour):

    flag = False
    rad = 10


    for y in range(yCoord, 100 + yCoord, 20):
        for x in range(xCoord, 100 + xCoord, 20):

            if flag:
                drawCircle(win, Point(x + rad, y + rad), rad, colour)
            elif x == xCoord or x == xCoord + 40 or x == xCoord + 80:
                drawTriangle(win, Point(x, y), Point(x + 20, y), Point(x + 10, y + 10), colour)
                drawTriangle(win, Point(x, y + 10), Point(x + 20, y + 10), Point(x + 10, y + 20), colour)
            else:
                drawTriangle(win, Point(x, y), Point(x, y + 20), Point(x + 10, y + 10), colour)
                drawTriangle(win, Point(x + 10, y), Point(x + 10, y + 20), Point(x + 20, y + 10), colour)

            flag = not flag

