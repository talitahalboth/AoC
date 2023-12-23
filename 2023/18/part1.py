import sys

path = []

max = [0,0,0,0]
directions = {'R': 0, 'U': 1, 'L': 2, 'D': 3}
neighbours = [(0, 1), (-1, 0), (0, -1), (1, 0)]

def coordCalc(x, y):
    return (x +  max[directions['L']] , y +  max[directions['U']] )

for l in sys.stdin:
    line = l.strip()
    list = line.split(' ')
    dir = list[0]
    count = int(list[1])
    max[directions[dir]]+=count
    path.append([dir, count])

grid = []
for i in range(0, max[directions['U']] + max[directions['D']] + 2):
    grid.append([])
    for i in range(0, max[directions['L']] + max[directions['R']] + 2):
        grid[-1].append('.')
prevX = 0
prevY = 0
for rule in path:
    dir = rule[0]
    dist = rule[1]
    (x, y) = neighbours[directions[dir]]
    curX = prevX + x*dist
    curY = prevY + y*dist
    a1 = 1 if dir != 'U' else -1
    a2 =  1 if dir != 'L' else -1
    for i in range(prevX, curX+a1,a1):
        for j in range(prevY, curY+a2,a2):
            (x,y) = coordCalc(i,j)
            grid[x][y] = '#'

    prevX = curX
    prevY = curY

def bfs(start, color):
    queue = []
    queue.append(start)
    while len(queue) > 0:
        (x,y) = queue.pop()
        grid[x][y] = color
        for n in neighbours:
            (x1, y1) = n
            newx = x + x1
            newy = y + y1
            if (newx < 0 or newx >= len(grid) or newy < 0 or newy >= len(grid[0])):
                continue
            if (grid[newx][newy] == '.'):
                queue.append((newx,newy))
res = 0
bfs((0,0), '*')
for row in grid:
    for cell in row:
        if (cell != '*'):
            res+=1
        print (cell, end='')
    print()
print()
print(res)