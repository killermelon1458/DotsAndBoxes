
width =1280
height = 720
numRows = 4
numCols =3
maxSquares = max(numCols,numRows)
spacing = round(min(width,height)/(maxSquares+3))
left = (width -(numCols*spacing))//2
top = (height - (numRows*spacing))//2
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

LoYMids = [[None for _ in range(numSquares+1)] for _ in range(numSquares)]
current = LoDots[0][0]
for col in range(numSquares+1):

    current = LoDots[0][col]
    for row in range(1,numSquares+1):
        
        LoYMids[row-1][col] = (LoDots[row][col][0],(current[1] + LoDots[row][col][1])/2)
        current = LoDots[row][col]


LoCenters = [[None for _ in range(numSquares)] for _ in range(numSquares)]


for row in range(numSquares):
    for col in range(numSquares):
        
        c1 = LoDots[row][col]       # Top-left
        c2 = LoDots[row][col+1]     # Top-right
        c3 = LoDots[row+1][col+1]   # Bottom-right
        c4 = LoDots[row+1][col]     # Bottom-left

        center_x = (c1[0] + c2[0] + c3[0] + c4[0]) / 4.0
        center_y = (c1[1] + c2[1] + c3[1] + c4[1]) / 4.0

        LoCenters[row][col] = (center_x, center_y)

    