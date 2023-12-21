import sys

times = 99
space = []
for line in sys.stdin:
    if not '#' in line:
        for xxx in range(0,times):
            space.append(line.strip())
    space.append(line.strip())
rows = []
for i in range(0, len(space[0])):
    hasGalaxy = False
    for j in range(0, len(space)):
        if (space[j][i] == '#'):
            hasGalaxy = True
    if not hasGalaxy:
        rows.append(i)
rows.reverse()
for i in rows:
    for j in range(0, len(space)):
        
        for xxx in range(0,times):
            space[j] = space[j][:i] + '.' + space[j][i:]
galaxies =[]
for i,row in enumerate(space):
    for j,x in enumerate(row):
        if (x == '#'):
            galaxies.append([i,j])
res = 0
for i in range(0, len(galaxies)):
    for j in range(i+1, len(galaxies)):
        [x,y] = galaxies[i]
        [x1,y1] = galaxies[j]
        val =  (abs(x-x1) + abs(y-y1))
        res  += val
        print('----------')
        print(i+1, ": ",x,y)
        print(j+1, ": ",x1,y1)
        print(val)
print(res)