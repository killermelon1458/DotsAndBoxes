import pygame
from box import *
from diamond import *
import random

class lineAndHitBox:
    def __init__(self, center, spacing, thickness, orientation):
        if orientation == 'level':
            line = box(center, spacing , thickness)
            hitbox= diamond.init_center(center,spacing)
        elif orientation == 'plumb':
            line = box(center, thickness,spacing)
            hitbox= diamond.init_center(center,spacing)
        else:
            raise ValueError("Orientation must be 'plumb' or 'level'.")
        self.orientation = orientation
        
    
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
    numSquares =5
    spacing = round(min(width,height)/(numSquares+3))
    left = (width -(numSquares*spacing))//2
    top = (height - (numSquares*spacing))//2
    halfSpace = round(spacing/2)
    clock = pygame.time.Clock()
    draw = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                draw = True
                click = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                click = (None,None)

            if draw:
                for row in range(numSquares+1):
                    x = left 
                    y = top
                    for col in range(numSquares+1):
                        midX = (x + left + col * spacing)/2
                        midY = (y +top + row * spacing)/2
                        x = left + col * spacing
                        y = top + row * spacing

                        pygame.draw.circle(win, 'black', (x,y), int(.2*spacing), 0)

            pygame.display.flip()
            clock.tick(10)

    pygame.quit()