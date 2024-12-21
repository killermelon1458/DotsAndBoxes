import pygame

class box:
    def __inti__(self, center,width,height, color='grey',outline=0,exists =False,):
        self.center = center
        self.width = width
        self.height = height
        self.color = color
        self.outline = outline
        self.exists = exists

    def draw(self, win):
        pygame.draw.rect(win,self.color,(self.x,self.y, self.width,self.height),self.outline)
    
    def getCenter(self):
        return self.center
    
    def exists(self):
        return self.exists
    
    def color(self):
        return self.color
    
    def isin(self, point):
        """Check if the point is within the square's boundaries"""
        px, py = point
        if self.x <= px <= self.x + self.width and self.y <= py <= self.y + self.height:
            return True
        return False
    
    def exists(self):
        return self.exists
    
    def setColor(self, color):
        self.color = color

    
    
    
