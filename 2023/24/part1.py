import sys
import math
import itertools as it
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Line(object):
    def __init__(self, ini, end):
        self.s = ini
        self.e = end

hailStones = []
area = Line(Point(200000000000000,200000000000000),Point(400000000000000,400000000000000))
dist = abs(math.ceil(math.sqrt(area.s.x**2 + area.e.x**2)))
for line in sys.stdin:
    l,r = line.strip().split('@')
    x,y,z = (int(s) for s in l.split(','))
    vx,vy,vz = (int(s) for s in r.split(','))
    
    NewTuple = (x,y,z, vx, vy, vz)
    hailStones.append(NewTuple)
hailStones.sort()
def findIntersection(line1: Line,line2: Line):
    a1 = line1.e.y - line1.s.y
    b1 = line1.s.x - line1.e.x
    c1 = a1 * line1.s.x + b1 * line1.s.y
    
    a2 = line2.e.y - line2.s.y
    b2 = line2.s.x - line2.e.x
    c2 = a2 * line2.s.x + b2 * line2.s.y

    delta = a1*b2 - a2*b1

    if (delta == 0):
        return Point(None, None)
    p1 = (b2*c1 - b1*c2)/delta
    p2 = (a1*c2 - a2*c1)/delta
    return Point(p1,p2)
res = 0
for A, B in it.combinations(hailStones, 2):
        
    (x,y,z, vx, vy, vz) = A
    p = Point(x,y)
    ex = p.x + vx * dist
    ey = p.y + vy * dist
    p1 = Point(ex,ey)
    line0 = Line(p,p1)

    (x1, y1, z1, vx1, vy1, vz1) = B
    p = Point(x1,y1)
    ex1 = p.x + vx1 * dist
    ey1 = p.y + vy1 * dist
    p1 = Point(ex1,ey1)
    line1 = Line(p,p1)

    p = findIntersection(line0, line1)
    x = p.x
    y = p.y
    if (x == None or y == None):
        continue

    if ((x < line0.s.x and vx > 0) or (x > line0.s.x and vx < 0) or (y < line0.s.y and vy > 0) or (y > line0.s.y and vy < 0)):
        continue
    if ((x < line1.s.x and vx1 > 0) or (x > line1.s.x and vx1 < 0) or (y < line1.s.y and vy1 > 0) or (y > line1.s.y and vy1 < 0)):
        continue
    if (x >= area.s.x and x <= area.e.x and y >= area.s.y and y <= area.e.y):
        res+=1
print(res)