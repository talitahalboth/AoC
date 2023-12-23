import sys

strToDir =  {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}
directions = {'R': 0, 'U': 1, 'L': 2, 'D': 3}
neighbours = [(0, 1), (-1, 0), (0, -1), (1, 0)]
coords = []
for l in sys.stdin:
    line = l.strip()
    list = line.split('#')[1][0:6]
    dir = strToDir[list[-1]]
    (row, col) = neighbours[directions[dir]]
    size =  int(list[:-1],16) 
    newRow = (coords[-1][0] if len(coords)> 0 else 0) + row*size 
    newCol =  (coords[-1][1] if len(coords)> 0 else 0) + col*size
    coords.append([newRow, newCol, dir])

for ix, [r, c, d] in enumerate(coords):
    next = (ix + 1) % len(coords)
    [nr,nc,nd] = coords[next]
    r+= 1 if d == 'L' or nd == 'L' else 0
    c+= 1 if d == 'D' or nd == 'D' else 0
    coords[ix] = [r,c,d]

sum = 0
[r0, c0, dir] = coords[-1]
for ix, [r, c, d] in enumerate(coords):
    h = (r + r0) / 2
    w = c0 - c
    a = h*w   
    sum+=a 
    r0 = r
    c0 = c
print(int(sum))