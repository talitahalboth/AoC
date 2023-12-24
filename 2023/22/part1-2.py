import sys
id = 0
space = {}
coords = {}
supports = {}
isSupported = {}
bricks = [ ]


for l in sys.stdin:
    line = l.strip()
    l, r = line.split('~')
    x0, y0 ,z0  = (int(s) for s in l.split(','))
    x1, y1, z1 = (int(s) for s in r.split(','))
    coords[id] = []
    supports[id] = set()
    isSupported[id] = set()

    for x in range(x0, x1+1):
        for y in range(y0, y1+1):
            for z in range(z0, z1+1): 
                space[(x,y,z)] = id     
                coords[id].append((x,y,z))
    id+=1

def fall():
    fell = 0
    for id in coords:
        flag = True
        for (x,y,z) in coords[id]:
            newKey = (x,y,z-1)
            if (z <= 1):
                flag = False
            if (newKey in space and space[newKey] != id):
                flag = False
        if (flag):
            fell+=1
            newArr = []
            for (x,y,z) in coords[id]:
                oldKey = (x,y,z)
                newKey = (x,y,z-1)
                newArr.append(newKey)
                del space[oldKey]
            coords[id] = []
            for elem in newArr:
                coords[id].append(elem)
                space[elem] = id
    if fell == 0:
        return False
    return True

while(True):
    if not fall():
        break
isGround = {}
for i in coords:
    for (x,y,z) in coords[i]:
        if (z == 1):
            isGround[i] = 1
        for j in coords:
            if (x,y,z+1) in coords[j]:
                if (j != i ):
                    supports[i].add(j)
                    isSupported[j].add(i)
single = set()

for id in isSupported:
    if (len(isSupported[id] )== 1):
        tmp = isSupported[id].pop()
        single.add(tmp)
        isSupported[id].add(tmp)
print(len(coords) - len(single))
res = 0
for i in isSupported:
    newSupports = {}
    for j in isSupported:
        newSupports[j] = set()
        for item in isSupported[j]:
            newSupports[j].add(item)
            
    queue = []
    queue.append(i)
    chain = set()
    count = 0
    while(len(queue) > 0):
        curr = queue.pop()
        for j in newSupports:
            if curr in newSupports[j]:
                newSupports[j].remove(curr)
                if (len(newSupports[j]) == 0):
                    queue.append(j)
    tmp = 0
    for j in newSupports:
        if (newSupports[j] != isSupported[j] and len(newSupports[j]) == 0 and j not in isGround):
            tmp+=1
    res+=tmp
print(res)