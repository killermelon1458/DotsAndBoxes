import pygame
from diamond import * 
class Rectangle:
    def __init__(self, x, y, width, height, color,outline = 0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.outline = outline

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height),self.outline)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def containsPoint(self, point):
        """Check if a point (x, y) is inside the rectangle."""
        px, py = point
        return (self.x <= px <= self.x + self.width) and (self.y <= py <= self.y + self.height)     
width =1280
height = 720
numSquares =10
pygame.init()
win = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
running = True
spacing = int(min(width,height)/(numSquares+3))
left = (width -(numSquares*spacing))//2
top = (height - (numSquares*spacing))//2
rectangle = Rectangle(100, 100, spacing, spacing, 'blue',int(5/numSquares))
testDiamond = diamond.init((left,top),(left,top+spacing))
testDiamond2 = diamond.init((left+2*spacing,top),(left+spacing,top))
testDiamond3 = diamond.init_point((left+2*spacing,2*spacing+top),spacing,'up')
testDiamond4 = diamond.init_center((left+spacing/2,top),spacing)
click =(0,0)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            click = (0,0)
    
    win.fill('grey')

    if testDiamond.isin(click):
        testDiamond.draw(win,'blue')
    if testDiamond2.isin(click):
        testDiamond2.draw(win,'green')
    if testDiamond3.isin(click):
        testDiamond3.draw(win,'red')
    if testDiamond4.isin(click):
        testDiamond4.draw(win,'yellow')

    for row in range(numSquares+1):
        for col in range(numSquares+1):
            x = left + col * spacing
            y = top + row * spacing

            pygame.draw.circle(win, 'black', (x,y), int(.2*spacing), 0)

    #pygame.draw.polygon(win,'yellow',[(200,200),(250,250),(200,300),(150,250)])
    
    #rectangle.draw(win)
    #if rectangle.containsPoint(click):
    
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        rectangle.move(-spacing, 0)
    if keys[pygame.K_d]:
        rectangle.move(spacing, 0)
    if keys[pygame.K_w]:
        rectangle.move(0, -spacing)
    if keys[pygame.K_s]:
        rectangle.move(0, spacing)


    pygame.display.flip()
    clock.tick(10)
pygame.quit()
#print(left)
