import sys
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
grid = []
for l in sys.stdin:
    line = l.strip()
    grid.append(list(line))

def printGridAndWait():
    cls()
    for row in grid:
        for cell in row:
            print(cell, end='')
        print()
    for x in range(0, 50000000):
        a = x
gridHistory = []
def compareGrids():
    for ix, g in enumerate(gridHistory):
        isEqual = True
        for i in range (0, len(grid)):
            for j in range (0, len(grid[i])):
                if (grid[i][j] != g[i][j]):
                    isEqual = False
                    break
            if not isEqual:
                break
        if (isEqual):
            return (True, ix)
    return (False, None)
count = 0
cycleSize = 0
cycleStart = 0
dif = 0
for dir in range(0, 1000):
    # printGridAndWait()

    y = [row[:] for row in grid]
    gridHistory.append(y)
    irange = range(0, len(grid))
    if (dir % 4 == 2): 
        irange = range(len(grid)-1, -1, -1)
    for i in irange:
        jrange = range(0, len(grid[i]))
        if (dir % 4 == 3):
            jrange = range(len(grid[i]) - 1, -1, -1)
        for j in jrange:
            if (grid[i][j] == 'O'):
                canMove = True
                vertical = i 
                horizontal = j 
                prevVertical = vertical
                prevHorizontal = horizontal
                if dir % 4 == 0:
                    vertical -= 1
                if dir % 4 == 1:
                    horizontal -= 1
                if dir % 4 == 2:
                    vertical += 1
                if dir % 4 == 3:
                    horizontal += 1

                while(canMove):
                    if (vertical < 0 or vertical >= len(grid) or horizontal < 0 or horizontal >= len(grid[i]) ):
                        canMove = False
                    else:
                        if (grid[vertical][horizontal] != '.'):
                            canMove = False
                    if (canMove):
                        grid[vertical][horizontal] = 'O'
                        grid[prevVertical][prevHorizontal] = '.'
                    
                    prevVertical = vertical
                    prevHorizontal = horizontal
                    if dir % 4 == 0:
                        vertical -= 1
                    if dir % 4 == 1:
                        horizontal -= 1
                    if dir % 4 == 2:
                        vertical += 1
                    if dir % 4 == 3:
                        horizontal += 1
    (isCycle, ix) = compareGrids()
    if isCycle and dif == 0:
        cycleSize = count - ix + 1
        print("index: ", ix)
        print("cycle length:", count)
        cycleStart = ix
        dif = count

        break
    
    count+=1
x = 1000000000*4
idx = (x - dif) % cycleSize + cycleStart
print(idx)
print(dif, cycleSize, cycleStart)
# res = gridHistory[idx]
print()
# for t in range(-10, 10):
res = 0
for i, row in enumerate( gridHistory[idx-1]):
    for cell in row:
        if cell == 'O':
            res += len(grid) - i
print( res)

