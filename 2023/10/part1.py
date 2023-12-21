import sys

adj=[]
row = 0
start = []

dists = []
for line in sys.stdin:
    dists.append([])
    if (len(adj) == 0):
        # for i in range(0, len(line)):
        adj.append([[]] * len(line))
    
    adj.append([[]] * len(line))
    for col, c in enumerate(line.strip()):
        dists[row].append(0)
        if (c == 'L'):
            adj[row][col] = [[row-1, col], [row, col+1]]
        if (c == 'F'):
            adj[row][col] = [[row, col+1], [row+1, col]]
        if (c == '7'):
            adj[row][col] = [[row, col-1], [row+1, col]]
        if (c == 'J'):
            adj[row][col] = [[row-1, col], [row, col-1]]
        if (c == '|'):
            adj[row][col] = [[row-1, col], [row+1, col]]
        if (c == '-'):
            adj[row][col] = [[row, col-1], [row, col+1]]
        if (c == 'S'):
            start = [row,col]
        
    row+=1
neighbours = [[0, 1], [0, -1], [1, 0], [-1, 0]]
startAdjs = []
for n in neighbours:
    row = start[0] + n[0]
    col = start[1] + n[1]
    if (start in adj[row][col]):
        startAdjs.append([row,col])
adj[start[0]][start[1]] = startAdjs
# for i, n in enumerate(adj):

next1 = adj[start[0]][start[1]][0]
row1 = next1[0]
col1 = next1[1]
next2 = adj[start[0]][start[1]][1]
row2 = next2[0]
col2 = next2[1]
dist = 1
prevRow1 = start[0]
prevCol1 = start[1]
prevRow2 = prevRow1
prevCol2 = prevCol1
while (dists[row1][col1] == 0 or dists[row2][col2] == 0):
    # break
    dists[row1][col1] = dist
    dists[row2][col2] = dist
    dist+=1
    adj1 = adj[row1][col1]
    if (adj1[0][0] == prevRow1 and adj1[0][1] == prevCol1):
        next1 = adj1[1]
    else:
        next1 = adj1[0]
    prevRow1 = row1
    prevCol1 = col1
    row1 = next1[0]
    col1 = next1[1]
    
    
    adj2 = adj[row2][col2]
    if (adj2[0][0] == prevRow2 and adj2[0][1] == prevCol2):
        next2 = adj2[1]
    else:
        next2 = adj2[0]
    prevRow2 = row2
    prevCol2 = col2
    row2 = next2[0]
    col2 = next2[1]
print(dist-1)