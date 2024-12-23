import pygame
from box import *
from diamond import *
import random

class lineAndHitBox:
    def __init__(self, box, diamond, orientation):
        self.line = box
        self.hitbox = diamond
        self.orientation = orientation
        if self.hitbox.getOrientation() == None:
            self.hitbox.setOrientation(orientation)

        
        
    
    def lineExists(self):
        return self.line.exists()
    
    def isin(self,click):
        return self.hitbox.isin(click)
    
    def setColor(self,color):
        self.line.setColor(color)

    def draw(self, win):
        self.line.draw(win)

    def getCenter(self):
        return self.line.getCenter()
    def testDraw(self, win):
        self.line.color =  'black'
        self.hitbox.color = random.choice(['yellow','red','blue','green','orange','purple'])
        self.hitbox.draw(win)
        self.line.draw(win)
def main():
    pygame.init()
    width =1280
    height = 720
    
    win = pygame.display.set_mode((width,height))
    numCols = 15
    numRows = 9
    
    maxSquares = max(numCols, numRows)
    minRes =min(width, height)
    resRatio = width/height
    dotsRatio = numCols/numRows
    
    if dotsRatio > resRatio:
    
        spacing = round( width/ (numCols + 3))
    elif resRatio >= dotsRatio:
        spacing = round( height/ (numRows + 3))

    left = (width - (numCols * spacing)) // 2
    top = (height - (numRows * spacing)) // 2            
    halfSpace = round(spacing/2)
    clock = pygame.time.Clock()
    click = (None,None)
    draw = True
    LoDots = [[None for _ in range(numCols + 1)] for _ in range(numRows + 1)]

    LoDia = [[] for _ in range((maxSquares * 2) + 1)]

    for row in range(numRows + 1):
        for col in range(numCols + 1):
            x = left + col * spacing
            y = top  + row * spacing
            LoDots[row][col] = (x, y)

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
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                draw = True
                click = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                click = (None,None)
            win.fill('grey')
            if draw:
                for i in range(len(LoDots)):
                    for j in range(len(LoDots[i])):
                        x = LoDots[i][j][0]
                        y = LoDots[i][j][1]
                        pygame.draw.circle(win, 'black', (x,y), int(.2*spacing), 0)
                for i in range(len(LoXMids)):
                    for j in range(len(LoXMids[i])):
                        x = LoXMids[i][j][0]
                        y = LoXMids[i][j][1]
                        pygame.draw.circle(win, 'black', (x,y), int(.15*spacing), 0) 
                for i in range(len(LoYMids)):
                    for j in range(len(LoYMids[i])):
                        x = LoYMids[i][j][0]
                        y = LoYMids[i][j][1]
                        pygame.draw.circle(win, 'black', (x,y), int(.15*spacing), 0) 
                for i in range(len(LoCenters)):
                    for j in range(len(LoCenters[i])):
                        x = LoCenters[i][j][0]
                        y = LoCenters[i][j][1]
                        pygame.draw.circle(win, 'black', (x,y), int(.1*spacing), 0) 

            pygame.display.flip() 
            clock.tick(10)

    pygame.quit()

main()