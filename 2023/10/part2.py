import sys

adj={}
row = 0
start = []

dists = []
grid = []
for line in sys.stdin:
    line = line.strip()
    dists.append([])
    grid.append([])
    for col, c in enumerate(line):
        grid[row].append(c)
        dists[row].append(0)
        if (c == 'L'):
            adj[(row,col)] = [(row-1, col), (row, col+1)]
        if (c == 'F'):
            adj[(row,col)] = [(row, col+1), (row+1, col)]
        if (c == '7'):
            adj[(row,col)] = [(row, col-1), (row+1, col)]
        if (c == 'J'):
            adj[(row,col)] = [(row-1, col), (row, col-1)]
        if (c == '|'):
            adj[(row,col)] = [(row-1, col), (row+1, col)]
        if (c == '-'):
            adj[(row,col)] = [(row, col-1), (row, col+1)]
        if (c == 'S'):
            start = (row,col)
        
    row+=1

N = len(grid)
M = len(grid[0])
neighbours = [[0, 1], [0, -1], [1, 0], [-1, 0]]
adj[(start[0],start[1])] = []
for n in neighbours:
    row = start[0] + n[0]
    col = start[1] + n[1]
    if ((row,col) in adj and start in adj[(row,col)]):
        adj[(start[0],start[1])].append((row,col))
reachable = {}
def bfs():
    queue = []
    queue.append(start)
    while(len(queue) > 0):
        top = queue.pop()
        (r,c) = top
        grid[r][c] = '#'
        reachable[top] = adj[top]
        for n in adj[top]:
            if n not in reachable:
                queue.append(n)
                reachable[n] = adj[n]
bfs()
ordered = sorted(reachable.items())
coords = []
[s, a] = ordered[0]
cur = a[0] if a[0][0] == s[0] else a[1]
(r,c) = s
coords.append((r,c,'R'))
prev = s
prevD = 'R'
dirByCoord = {}
dirByCoord[(r,c)] = 'R'
while(cur != s):
    adjs = adj[cur]
    next = adjs[0] if adjs[0] != prev else adjs[1]
    curR, curC = cur
    nextR, nextC = next
    d = 'R'
    if (nextC > curC):
        d = 'R'
    if (nextC < curC):
        d = 'L'
    if (nextR > curR):
        d = 'D'
    if (nextR < curR):
        d = 'U'
    if (d != prevD):
        coords.append((curR, curC, d))
    prevD = d
    prev = cur
    cur = next

def colour(start):
    queue = []
    (r,c) = start
    if (grid[r][c] != '#'):
        queue.append(start)
    else:
        return
    while(len(queue)> 0):
        top = queue.pop()
        (r,c) = top
        grid[r][c] = 'I'
        for n in neighbours:
            row = r + n[0]
            col = c + n[1]
            if (grid[row][col] != '#' and grid[row][col] != 'I'):
                queue.append((row,col))

[r0, c0, d0] = coords[-1]
for [r, c, d] in coords:
    next = []
    if ((d0 == 'R' and d == 'U') or (d0 == 'U' and d == 'R')):
        next.append((r+1, c+1))
        next.append((r+1, c))
        next.append((r, c+1))
    if ((d0 == 'R' and d == 'D') or (d0 == 'D' and d == 'R')):
        next.append((r+1, c-1))
        next.append((r+1, c))
        next.append((r, c-1))
    if ((d0 == 'L' and d == 'D') or (d0 == 'D' and d == 'L')):
        next.append((r-1, c-1))
        next.append((r-1, c))
        next.append((r, c-1))
    if ((d0 == 'L' and d == 'U') or (d0 == 'U' and d == 'L')):
        next.append((r-1, c+1))
        next.append((r-1, c))
        next.append((r, c+1))
    for n in next:
        colour(n)
    r0 = r
    c0 = c
    d0 = d
res = 0
for i in grid:
    for  j in i:
        if (j == 'I'):
            res+=1

print(res)