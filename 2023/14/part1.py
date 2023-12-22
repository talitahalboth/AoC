import sys

grid = []
for l in sys.stdin:
    line = l.strip()
    grid.append(list(line))

for i, row in enumerate(grid):
    for j, cell in enumerate(grid[i]):
        if (grid[i][j] == 'O'):
            canMoveUp = True
            north = i-1
            while(canMoveUp):
                if (north < 0):
                    canMoveUp = False
                else:
                    if (grid[north][j] != '.'):
                        canMoveUp = False
                if (canMoveUp):
                    grid[north][j] = 'O'
                    grid[north+1][j] = '.'
                north-=1
res = 0
for i, row in enumerate(grid):
    for cell in row:
        if cell == 'O':
            res += len(grid) - i
print(res)

