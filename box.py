import pygame

class box:
    def __init__(self, center,width,height, color='grey',outline=0,exists =False,):
        self.center = center
        self.width = width
        self.height = height
        self.color = color
        self.outline = outline
        self.exists = exists
        self.drawX = self.center[0] - self.width/2+1
        self.drawY = self.center[1] - self.height/2+1

    def draw(self, win):
        pygame.draw.rect(win,self.color,(self.drawX,self.drawY, self.width,self.height),self.outline)
    
    def getCenter(self):
        return self.center
    
    def doesExist(self):
        return self.exists
    
    def setExists(self,exists):
        if exists:
            self.exists = exists
        else:
            self.exists = False
    
    def getColor(self):
        return self.color
    
    def isin(self, point):
        """Check if the point is within the square's boundaries"""
        px, py = point
        if self.x <= px <= self.x + self.width and self.y <= py <= self.y + self.height:
            return True
        return False
    
    
    
    def setColor(self, color):
        self.color = color

    
    
    
