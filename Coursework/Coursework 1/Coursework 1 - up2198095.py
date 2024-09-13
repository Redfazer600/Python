##############################
# Alexander Bevan
# Programming Coursework 1 - Patchwork
# UP2198095
# Due date: 11/12/23 16:00 GMT
##############################

# Imports
from graphics import *

# Simple Functions - used within the patch designs
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


def drawRectangle(win, point1, point2, colour):
    rec = Rectangle(point1, point2)
    rec.setFill(colour)
    rec.draw(win)


# Patch design functions
def drawPenultimatePatch(win, xCoord, yCoord, colour):

    flag = False
    rad = 10
    xCoord = int(xCoord)
    yCoord = int(yCoord)

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


# Other functions
def getPatchworkSize():
    while True:
        patchworkSize = input('Please enter either 5/7/9 for the corresponding grid size 5x5/7x7/9x9\t')
        if not patchworkSize.isdigit():
            print('\nYou have entered a letter ya dummy! try entering a number this time - either 5, 7 or 9')
        elif int(patchworkSize) in [5, 7, 9]:
            patchworkSize = int(patchworkSize)
            print(f'\nthank you, you have chosen a {patchworkSize}x{patchworkSize} grid')
            break
        else:
            print('\nYou have not entered a valid number!')
    return patchworkSize


def getFirstColour(colourList):
    while True:
        col1 = input(f'\nPlease enter a colour out of the following choices: {colourList}\t')
        col1 = col1.lower()
        if col1 in colourList:
            print('Cool, thanks for entering a listed colour!!')
            break
        elif not col1.isalnum():
            print(f'\nThat is a special colour, we want regular colours, pick from {colourList} please!')
        elif not col1.isalpha():
            print(f'\numm, since when have colours contained numbers? pick from {colourList}\t')
        else:
            print(f'\nhey... the user is not using the list of colours in lego city... use it! pick from {colourList}')

    return col1


def getSecondColour(colourList, col1):
    while True:
        col2 = input(f'\nPlease enter another colour but not {col1}: {colourList}\t')
        col2 = col2.lower()
        if col2 in colourList and col2 != col1:
            print('Awesome, you can follow instructions, good to know.  ')
            break
        elif col2 == col1:
            print(f'Oh, was it not clear? I need one from {colourList} but not {col1}!')
        elif not col2.isalnum():
            print(f'\nThat is a special colour, we want regular colours, pick from {colourList} please!')
        elif not col2.isalpha():
            print(f'\numm, since when have colours contained numbers? pick from {colourList}\t')
        else:
            print(f'\nhey... the user is not using the list of colours in lego city... use it! pick from {colourList}')

    return col2


def getThirdColour(colourList, col1, col2):
    while True:
        col3 = input(f'\nLast time, I promise. Another colour but not {col1} or {col2}: {colourList}\t')
        col3 = col3.lower()
        if col3 in colourList and col3 != col1 and col3 != col2:
            print('Sweet, now we can get on with the patchwork! Finally!!')
            break
        elif col3 == col1:
            print(f'Come on!!!You have done it once already! I need one from {colourList} but not {col1} or {col2}!')
        elif col3 == col2:
            print(f'Come on!!!You have done it once already! I need one from {colourList} but not {col1} or {col2}!')
        elif not col3.isalnum():
            print(f'\nThat is a special colour, we want regular colours, pick from {colourList} please!')
        elif not col3.isalpha():
            print(f'\numm, since when have colours contained numbers? pick from {colourList}\t')
        else:
            print(f'\nhey... the user is not using the list of colours in lego city... use it! pick from {colourList}')

    return col3


def drawPatchwork(win, currentPosition, list, list2, list3, col1, col2, col3):
    for iteration in list:
        if currentPosition.getX() == iteration.getX() and currentPosition.getY() == iteration.getY():
            drawFinalPatch(win, currentPosition.getX(), currentPosition.getY(), col1)

    for iteration in list2:
        if currentPosition.getX() == iteration.getX() and currentPosition.getY() == iteration.getY():
            drawPenultimatePatch(win, currentPosition.getX(), currentPosition.getY(), col2)

    for iteration in list3:
        if currentPosition.getX() == iteration.getX() and currentPosition.getY() == iteration.getY():
            drawPenultimatePatch(win, currentPosition.getX(), currentPosition.getY(), col3)

def drawSquares(win, currentPosition, list, list2, list3, col1, col2, col3):
    for iteration in list:
        if currentPosition.getX() == iteration.getX() and currentPosition.getY() == iteration.getY():
            drawRectangle(win, currentPosition, Point(currentPosition.getX() + 100, currentPosition.getY() + 100), col1)

    for iteration in list2:
        if currentPosition.getX() == iteration.getX() and currentPosition.getY() == iteration.getY():
            drawRectangle(win, currentPosition, Point(currentPosition.getX() + 100, currentPosition.getY() + 100), col2)

    for iteration in list3:
        if currentPosition.getX() == iteration.getX() and currentPosition.getY() == iteration.getY():
            drawRectangle(win, currentPosition, Point(currentPosition.getX() + 100, currentPosition.getY() + 100), col3)


########## Main Code ##########

def main():

    # Lists & predefined variables
    colourList = ['red', 'green', 'blue', 'magenta', 'orange', 'yellow', 'cyan']

    final5x5 = [Point(100, 100), Point(300, 100), Point(100, 300), Point(300, 300), Point(200, 200)]
    penultimate5x5C2 = [Point(200, 100), Point(200, 300)]
    penultimate5x5C3 = [Point(100, 200), Point(300, 200)]
    col1Squares5x5 = [Point(0, 0), Point(400, 0), Point(0, 400), Point(400, 400)]
    col2Squares5x5 = [Point(100, 0), Point(200, 0), Point(300, 0), Point(100, 400), Point(200, 400), Point(300, 400)]
    col3Squares5x5 = [Point(0, 100), Point(0, 200), Point(0, 300), Point(400, 100), Point(400, 200), Point(400, 300)]

    final7x7 = [Point(100, 100), Point(200, 200), Point(300, 300), Point(400, 400), Point(500, 500),
                Point(100, 500), Point(200, 400), Point(400, 200), Point(500, 100)]
    penultimate7x7C2 = [Point(200, 100), Point(300, 100), Point(400, 100), Point(300, 200),
                        Point(300, 400), Point(200, 500), Point(300, 500), Point(400, 500)]
    penultimate7x7C3 = [Point(100, 200), Point(100, 300), Point(100, 400), Point(200, 300),
                        Point(400, 300), Point(500, 200), Point(500, 300), Point(500, 400)]
    col1Squares7x7 = [Point(0, 0), Point(600, 0), Point(0, 600), Point(600, 600)]
    col2Squares7x7 = [Point(100, 0), Point(200, 0), Point(300, 0), Point(400, 0),
                      Point(500, 0), Point(500, 600), Point(100, 600),
                      Point(200, 600), Point(300, 600), Point(400, 600), Point(500, 600)]
    col3Squares7x7 = [Point(0, 100), Point(0, 200), Point(0, 300), Point(0, 400), Point(0, 500),
                      Point(600, 100), Point(600, 200), Point(600, 300),
                      Point(600, 400), Point(600, 500)]

    final9x9 = [Point(100, 100), Point(200, 200), Point(300, 300), Point(400, 400), Point(500, 500), Point(600, 600),
                Point(700, 700), Point(700, 100), Point(600, 200), Point(500, 300), Point(400, 400),
                Point(300, 500), Point(200, 600), Point(100, 700)]
    penultimate9x9C2 = [Point(200, 100), Point(300, 100), Point(400, 100), Point(500, 100), Point(600, 100),
                        Point(300, 200), Point(400, 200), Point(500, 200), Point(400, 300), Point(400, 500),
                        Point(300, 600), Point(400, 600), Point(500, 600), Point(200, 700), Point(300, 700),
                        Point(400, 700), Point(500, 700), Point(600, 700)]
    penultimate9x9C3 = [Point(100, 200), Point(100, 300), Point(100, 400), Point(100, 500), Point(100, 600),
                        Point(200, 300), Point(200, 400), Point(200, 500), Point(300, 400), Point(500, 400),
                        Point(600, 300), Point(600, 400), Point(600, 500), Point(700, 200), Point(700, 300),
                        Point(700, 400), Point(700, 500), Point(700, 600)]
    col1Squares9x9 = [Point(0, 0), Point(800, 0), Point(0, 800), Point(800, 800)]
    col2Squares9x9 = [Point(100, 0), Point(200, 0), Point(300, 0), Point(400, 0),
                      Point(500, 0), Point(600, 0), Point(700, 0), Point(100, 800),
                      Point(200, 800), Point(300, 800), Point(400, 800), Point(500, 800),
                      Point(600, 800), Point(700, 800)]
    col3Squares9x9 = [Point(00, 100), Point(00, 200), Point(00, 300), Point(00, 400),
                      Point(00, 500), Point(00, 600), Point(00, 700), Point(800, 100),
                      Point(800, 200), Point(800, 300), Point(800, 400), Point(800, 500),
                      Point(800, 600), Point(800, 700)]

    patchworkSize = getPatchworkSize()
    stepSize = 100
    col1 = getFirstColour(colourList)
    col2 = getSecondColour(colourList, col1)
    col3 = getThirdColour(colourList, col1, col2)

    winSize = 100 * int(patchworkSize)
    win = GraphWin('Patchwork', winSize, winSize)
    print(winSize)

    for y in range(0, winSize, 100):
        for x in range(0, winSize, 100):
            currentPosition = Point(x, y)
            if patchworkSize == 5:
                drawPatchwork(win, currentPosition, final5x5, penultimate5x5C2, penultimate5x5C3, col1, col2, col3)
                drawSquares(win, currentPosition, col1Squares5x5, col2Squares5x5, col3Squares5x5, col1, col2, col3)

            elif patchworkSize == 7:
                drawPatchwork(win, currentPosition, final7x7, penultimate7x7C2, penultimate7x7C3, col1, col2, col3)
                drawSquares(win, currentPosition, col1Squares7x7, col2Squares7x7, col3Squares7x7, col1, col2, col3)

            elif patchworkSize == 9:
                drawPatchwork(win, currentPosition, final9x9, penultimate9x9C2, penultimate9x9C3, col1, col2, col3)
                drawSquares(win, currentPosition, col1Squares9x9, col2Squares9x9, col3Squares9x9, col1, col2, col3)

    win.getMouse()
    win.close()



main()
