import pygame
from box import *
from diamond import *
import random

class lineAndHitBox:
    def __init__(self, box,outline, diamond, orientation):
        self.line = box
        self.outline = outline
        self.hitbox = diamond
        self.orientation = orientation
        if self.hitbox.getOrientation() == None:
            self.hitbox.setOrientation(orientation)
        self.exists = False

        
    def setExists(self, exists):
        self.line.setExists(exists)    
        self.outline.setExists(exists)
        self.exists = True
    
    def doesExist(self):
        return self.line.doesExist()
    
    def isin(self,click):
        return self.hitbox.isin(click)
    
    def setColor(self,color):
        if self.doesExist():
            pass
        else:
            self.line.setColor(color)

    def getColor(self):
        return self.line.getColor()

    def draw(self, win):
        self.outline.draw(win)
        self.line.draw(win)
        

    def getCenter(self):
        return self.line.getCenter()
    def testDraw(self, win):
        self.line.color =  'black'
        #color = random.choice(['yellow','red','blue','green','orange','purple','white','tan','brown','teal','lavender'])
        self.hitbox.draw(win,randomRGB())
        self.line.draw(win)

def calcSpacing(width,height,numCols,numRows):
    resRatio = width/height
    dotsRatio = numCols/numRows
    
    if dotsRatio > resRatio:
    
        spacing = round( width/ (numCols + 3))
    elif resRatio >= dotsRatio:
        spacing = round( height/ (numRows + 3))
    return spacing

def makeDotPoints(width,height,numCols,numRows,spacing):

    left = (width - (numCols * spacing)) // 2
    top = (height - (numRows * spacing)) // 2            
    
    LoDots = [[None for _ in range(numCols + 1)] for _ in range(numRows + 1)]

    
    for row in range(numRows + 1):
        for col in range(numCols + 1):
            x = left + col * spacing
            y = top  + row * spacing
            LoDots[row][col] = (x, y)
    return LoDots

def calcPoints(LoDots,numCols,numRows):
    LoXMids = [[None for _ in range(numCols)] for _ in range(numRows + 1)]

    for row in range(numRows + 1):
        # Start from the leftmost dot in this row
        current = LoDots[row][0]
        # Compute midpoints between successive columns in the same row
        for col in range(1, numCols + 1):
            LoXMids[row][col - 1] = (
                (current[0] + LoDots[row][col][0]) / 2.0, 
                LoDots[row][col][1]
            )
            current = LoDots[row][col]
 
    LoYMids = [[None for _ in range(numCols + 1)] for _ in range(numRows)]

    for col in range(numCols + 1):
        # Start from the top dot in this column
        current = LoDots[0][col]
        # Compute midpoints between successive rows in the same column
        for row in range(1, numRows + 1):
            LoYMids[row - 1][col] = (
                LoDots[row][col][0], 
                (current[1] + LoDots[row][col][1]) / 2.0
            )
            current = LoDots[row][col]

    LoCenters = [[None for _ in range(numCols)] for _ in range(numRows)]

    for row in range(numRows):
        for col in range(numCols):
            c1 = LoDots[row][col]       # Top-left
            c2 = LoDots[row][col + 1]   # Top-right
            c3 = LoDots[row + 1][col + 1]  # Bottom-right
            c4 = LoDots[row + 1][col]   # Bottom-left
            center_x = (c1[0] + c2[0] + c3[0] + c4[0]) / 4.0
            center_y = (c1[1] + c2[1] + c3[1] + c4[1]) / 4.0
            LoCenters[row][col] = (center_x, center_y)
    return LoXMids,LoYMids,LoCenters

def createLines(LoPoints,spacing,orient):
    halfSpace = round(spacing/2)
    LoLines= []
    LoOutlines = []
    for i in range(len(LoPoints)):
        row = []
        outRow = []
        for j in range(len(LoPoints[i])):
            dia =diamond.init_center(LoPoints[i][j],spacing-2)
            dia.setOrientation(orient)
            if orient == 'level':
                line = box((LoPoints[i][j][0],LoPoints[i][j][1]),spacing,.15*spacing)
                outline = box((LoPoints[i][j][0],LoPoints[i][j][1]),spacing,.15*spacing+2)
                outline.setColor('black')
            elif orient == 'plumb':
                line = box((LoPoints[i][j][0],LoPoints[i][j][1]),.15*spacing,spacing)
                outline = box((LoPoints[i][j][0],LoPoints[i][j][1]),.15*spacing+2,spacing)
                outline.setColor('black')
            else:
                raise ValueError("orient needs to be 'level' or 'plumb'")
            stick = lineAndHitBox(line,outline,dia,orient)

            row.append(stick)
            
        LoLines.append(row)
    
    return LoLines
def createBoxes(LoCenters,spacing):
    LoSquares =[]
    for i in range(len(LoCenters)):
        row =[]
        for j in range(len(LoCenters[i])):
            row.append(box(LoCenters[i][j],spacing,spacing))
        LoSquares.append(row)
    return LoSquares

def randomRGB():
    r= random.choice(range(255))
    g= random.choice(range(255))
    b= random.choice(range(255))
    return (r,g,b)

def drawDots(LoDots,win,spacing):
    for i in range(len(LoDots)):
        for j in range(len(LoDots[i])):
            x = LoDots[i][j][0]
            y = LoDots[i][j][1]
            pygame.draw.circle(win, 'black', (x,y), int(.2*spacing), 0)
    for i in range(len(LoDots)):
        for j in range(len(LoDots[i])):
            x = LoDots[i][j][0]
            y = LoDots[i][j][1]
            pygame.draw.circle(win, (61, 61, 61), (x,y), int(.179*spacing), 0)

def cliclStick(LoSticks,click,color):
    for i in range(len(LoSticks)):
        for j in range(len(LoSticks[i])):
            if LoSticks[i][j].isin(click):
                LoSticks[i][j].setColor(color)
                LoSticks[i][j].setExists(True)

def drawSticks(LoSticks,win):
    for i in range(len(LoSticks)):
        for j in range(len(LoSticks[i])):
            if LoSticks[i][j].doesExist():
                LoSticks[i][j].draw(win)

def checkBoxEnclosed(LoLevelSticks,LoPlumbSticks,LoSquares,turn):
    for row in range(len(LoSquares)):
        for col in range(len(LoSquares[row])):
            if not LoSquares[row][col].doesExist():
                if LoLevelSticks[row][col].doesExist() and LoLevelSticks[row+1][col].doesExist()\
                and LoPlumbSticks[row][col].doesExist() and LoPlumbSticks[row][col+1].doesExist():
                    LoSquares[row][col].setExists(True)
                    #if turn == LoLevelSticks[row][col].getColor() or turn == LoLevelSticks[row+1][col].getColor()\
                    #or turn == LoPlumbSticks[row][col].getColor() or turn == LoPlumbSticks[row][col+1].getColor():
                    LoSquares[row][col].setColor(turn)

def drawSquares(LoSquares,win):
    for row in range(len(LoSquares)):
        for col in range(len(LoSquares[row])):
            if LoSquares[row][col].doesExist():
                LoSquares[row][col].draw(win)
                


def main():
    
    width =1500
    height = 750
    
    numCols = 75
    numRows = 37
    spacing = calcSpacing(width,height,numCols,numRows)
    LoDots = makeDotPoints(width,height,numCols,numRows,spacing)
    [LoXMids,LoYMids,LoCenters] =calcPoints(LoDots,numCols,numRows)
    LoLevelSticks = createLines(LoXMids,spacing,'level')
    LoPlumbSticks = createLines(LoYMids,spacing,'plumb')
    LoSquares = createBoxes(LoCenters,spacing)
    
    pygame.init()
    win = pygame.display.set_mode((width,height))
    clock = pygame.time.Clock()
    click = (0,0)
    running = True
    
    draw = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                draw = True
                click = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                draw = False
                click = (0,0)
            
            
            
            if draw:
                win.fill('grey')
                """
                for i in range(len(LoSquares)):
                    for j in range(len(LoSquares[i])):
                        #color = random.choice(['yellow','red','blue','green','orange','purple','white','tan','brown','teal','lavender'])
                        color = 'blue'
                        LoSquares[i][j].setColor(color)
                        LoSquares[i][j].draw(win)                
                """
                ranColor = randomRGB()
                cliclStick(LoLevelSticks,click,ranColor)
                cliclStick(LoPlumbSticks,click,ranColor)
                checkBoxEnclosed(LoLevelSticks,LoPlumbSticks,LoSquares,ranColor)
                drawSquares(LoSquares,win)
                
                drawSticks(LoLevelSticks,win)
                drawSticks(LoPlumbSticks,win)
                drawDots(LoDots,win,spacing)
                
                        
            pygame.display.flip() 
            clock.tick(60)

    pygame.quit()

main()