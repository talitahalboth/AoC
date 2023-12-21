import sys

extraRows = []
extraColumns = []
space = []
columns = []
galaxies =[]
times = 1000000 - 1
for line in sys.stdin:
    if not '#' in line:
        columns.append(times)
    else:
        columns.append(0)
        indices = [i for i, x in enumerate(line) if x == '#']
        for i in indices:
            galaxies.append([len(space), i])
    space.append(line.strip())
rows = []
for i in range(0, len(space)):
    hasGalaxy = False
    extraColumns.append(0)
    extraRows.append(0)
    for j in range(0, len(space)):
        if (space[j][i] == '#'):
            hasGalaxy = True
    if not hasGalaxy:
        rows.append(times)
    else:
        rows.append(0)
for i in range(0, len(extraColumns)):
    res = 0
    if (i > 0):
        res = extraColumns[i-1] 
    extraColumns[i] += res + columns[i]
for i in range(0, len(extraRows)):
    res = 0
    if (i > 0):
        res = extraRows[i-1] 
    extraRows[i] += res + rows[i]
res = 0
for i in range(0, len(galaxies)):
    for j in range(i+1, len(galaxies)):
        [x,y] = galaxies[i]
        [x1,y1] = galaxies[j]
        disx = abs(extraColumns[x] - extraColumns[x1])
        disy = abs(extraRows[y] - extraRows[y1])
        val =  abs(x-x1) + abs(y-y1) + disx + disy
        res  += val
print(res)