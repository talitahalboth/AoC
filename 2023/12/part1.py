import sys

grid = []
rules = []

def printRow(row):
    for c in row:
        if c == -1:
            print('?', end='')
        if c == 0:
            print('.', end='')
        if c == 1:
            print('#', end='')
    print()

def checkValid(row: list, rules):
    ix = 0
    ruleIx = 0
    next = 1
    ret = True
    res = 0
    row.append(0)
    while(next in row[ix:]):
        res = row[ix:].index(next)
        ix += res
        if (next == 0):
            if (ruleIx >= len(rules)):
                ret = False
            elif (res != int(rules[ruleIx])):
                ret = False
            ruleIx+=1
        next = 1 if (next == 0) else 0
    if (ruleIx < len(rules)):
        ret = False
    row.pop(len(row)-1)
    return ret


def pd( posRow, posRules, used,  row, rules, arr):
    if (posRules < len(rules) and used == rules[posRules]):
        if not checkValid(row[:posRow], rules[:posRules+1]):
            return 0
        posRules = posRules + 1
        used = 0
    if (posRules >= len(rules)):
        if (posRow >= len(arr)):
            return 1 if checkValid(row[:posRow], rules) else 0
        if row[posRow] == -1:
            row[posRow] = 0
            res = pd(posRow+1, posRules, used, row, rules, arr)
            row[posRow] = -1
            return res
        return  pd(posRow+1, posRules, used, row, rules, arr)
    
    if (posRow >= len(arr)):
        return 0
    if (used > rules[posRules]):
        return 0
    

    op1=0
    op2=0
    if row[posRow] == -1:
        row[posRow] = 0
        op1 = pd(posRow+1, posRules, used, row, rules, arr)
        row[posRow] = 1
        op2 = pd(posRow+1, posRules, used+1, row, rules, arr)
        row[posRow] = -1
    elif row[posRow] == 0:
        op1 = pd(posRow+1, posRules, used, row, rules, arr)
    elif row[posRow] == 1:
        op1 = pd(posRow+1, posRules, used+1, row, rules, arr)
        

    return op1 + op2


res = 0
for l in sys.stdin:
    line = l.strip().split(' ')
    
    row = []
    for c in  line[0]:
        new = -1
        if (c == '.'):
            new = 0
        if (c == '#'):
            new = 1
        row.append(new)

    rulesStr = line[1].split(',')
    rules = []
    for r in rulesStr:
        rules.append(int(r))
    arr = [[[[-1 for i in range(3)]for i in range(len(row))] for i in range(len(rules))] for j in range(len(row))]
    res+=(pd(0,0,0,row,rules,arr))
print (res)