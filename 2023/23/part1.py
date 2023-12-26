import sys

sys.setrecursionlimit(10000)
grid = {}
neighbours = [(0, -1), (0, 1), (-1, 0), (1, 0)]
dists = {}
start = 0
graph = {}
saida = {}
lines = 0
width = 0
for line in sys.stdin:
    line = line.strip()
    width = len(line)
    for ix, c in enumerate(line):
        key = (lines, ix)
        graph[key] = []
        if c == '.': 
            if start == 0:
                start = key
            saida = key
        if (c != '#'):
            grid[key] = c
    lines+=1

maxSteps = 0
def dfs(grid, visited, pd, node, count):
    if (grid[node] == '#'):
        return
    if (node in visited and visited[node] ):
        return
    visited[node] = True
    if node not in pd:
        pd[node]=  0
    pd[node] = max(pd[node], count)
    c = grid[node]
    (x0, y0) = node
    # x1,y1 = (0,1)
    # if c == 'v':
    #     x1,y1 = (1, 0)
    # elif c == '<':
    #     x1,y1 = (0, -1)
    # elif c == '^':
    #     x1,y1 = (-1, 0)
    # viz = [(x1, y1)]
    
    # if (c == '.'):
    viz = neighbours
    
    for v in viz:
        (x1,y1) = v
        x = x0 + x1
        y = y0 + y1
        newNode = (x,y)
        if newNode in grid:
            dfs(grid, visited, pd, newNode, count+1)
    visited[node] = False


vis = {}
pd = {}
dfs(grid, vis, pd, start, 0)
print(pd[saida])