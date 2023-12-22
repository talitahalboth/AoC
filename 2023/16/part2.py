import sys

directions = {'l': [0, -1],'r': [0, 1],'u': [-1, 0],'d': [1, 0]}
COORD = 'COORD'
DIR = 'DIR'
grid = []
for l in sys.stdin:
    line = l.strip()
    grid.append(line)
        
def updatePosition(cur, direction):
    next = directions[direction]
    new = [cur[0] + next[0], cur[1] + next[1]]
    return new

maxi = 0
for d in directions:
    for i in range(0, len(grid)):
        coord = []
        if (d == 'r'):
            coord = [i, 0]
        if (d == 'l'):
            coord =  [i,len(grid)-1]
        if (d == 'd'):
            coord = [0, i]
        if (d == 'u'):
            coord = [len(grid)-1, i]

        beams = [{COORD:coord, DIR: d}]
        
        tiles = []
        for x in grid:
            tiles.append([])
            tiles[-1] = []
            for y in x:
                tiles[-1].append({})
        def update(coord, direction):
            next = updatePosition(coord,direction)
            x = next[0]
            y = next[1]
            if (x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) ):
                return
            if not direction in tiles[x][y]:
                beams.append({COORD: [x, y], DIR: direction})
                tiles[x][y][direction] = 1


        while(len(beams) > 0):
            curr = beams.pop()
            coord = curr[COORD]
            direction =  curr[DIR]
            
            curX = coord[0]
            curY = coord[1]
            if not direction in tiles[curX][curY]:
                tiles[curX][curY][direction] = 1
            
            if (grid[curX][curY] == '.'):
                update(coord, direction)
            elif (grid[curX][curY] == '|'):
                if (direction == 'u' or direction == 'd'):
                    update(coord, direction)
                else:
                    update(coord, 'u')
                    update(coord, 'd')
            elif (grid[curX][curY] == '-'):
                if (direction == 'l' or direction == 'r'):
                    update(coord, direction)
                else:
                    update(coord, 'l')
                    update(coord, 'r')
            elif (grid[curX][curY] == "\\"):
                if (direction == 'r'):
                    update(coord, 'd')

                elif (direction == 'l'):
                    update(coord, 'u')

                elif (direction == 'd'):
                    update(coord, 'r')

                elif (direction == 'u'):
                    update(coord, 'l')

            elif (grid[curX][curY] == '/'):
                if (direction == 'r'):
                    update(coord, 'u')

                elif (direction == 'l'):
                    update(coord, 'd')

                elif (direction == 'd'):
                    update(coord, 'l')
                    
                elif (direction == 'u'):
                    update(coord, 'r')

        res = 0
        i = 0
        for t in tiles:
            j = 0
            for cell in t:
                if (len(cell) > 0):
                    res +=1
        maxi = max(res, maxi) 
print(maxi)