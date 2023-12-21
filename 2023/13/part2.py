import sys

def solvePattern(pattern):
    for cut in range(1, len(pattern) ):
        isSame = True
        numDif = 0
        for j in range(0, cut):
            u = cut - j - 1
            d = cut + j
            if u >= 0 and d < len(pattern):
                for i in range(0, len(pattern[u])):
                    if (pattern[u][i] != pattern[d][i]):
                        numDif+=1
        if numDif == 1:
            return cut*100
    for cut in range(1,len(pattern[0])):
        isSame = True
        numDif = 0
        for j in range(0, cut):
            l = cut - j - 1
            r = cut + j
            if l >= 0 and r < len(pattern[0]):
                for i in range(0, len(pattern)):
                    if (pattern[i][l] != pattern[i][r]):
                        numDif +=1
        if numDif == 1:
            return cut
    return 0



pattern = []
res = 0
for l in sys.stdin:
    line = l.strip()
    if (len(line) > 0):
        pattern.append(line)
    else:
        res += solvePattern(pattern)
        pattern = []

res += solvePattern(pattern)
print(res)