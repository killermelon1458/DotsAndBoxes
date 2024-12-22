
width =1280
height = 720

numSquares =5
spacing = round(min(width,height)/(numSquares+3))
left = (width -(numSquares*spacing))//2
top = (height - (numSquares*spacing))//2
halfSpace = round(spacing/2)
x = left 
y = top
click = (None,None)
draw = True
LoDots = [[None for _ in range(numSquares + 1)] for _ in range(numSquares + 1)]
LoDia = [[]]*((numSquares*2)+1)
for row in range(numSquares + 1):
    for col in range(numSquares + 1):
        x = left + col * spacing
        y = top  + row * spacing
        LoDots[row][col] = (x, y)
  
LoXMids = [[None for _ in range(numSquares)] for _ in range(numSquares+1)]
current = LoDots[0][0]
for row in range(numSquares+1):
    current = LoDots[row][0]
    for col in range(1,numSquares+1):
        
        LoXMids[row][col-1] = ((current[0] + LoDots[row][col][0])/2,LoDots[row][col][1])
        current = LoDots[row][col]