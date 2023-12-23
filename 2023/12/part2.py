import sys

UKNOWN = '?'
WORKING = '.'
DAMAGED = '#'

grid = []
rules = []

dp = {}
def pd( posRow, posRules, used,  row, rules):
    
    key = (posRow,posRules,used)
    if (key in dp):
        return dp[key]
    if (posRow == len(row)):
        if posRules==len(rules) and used == 0:
            return 1
        elif posRules==len(rules) -1 and used == rules[posRules]:
            return 1
        else:
            return 0

    res = 0
    if (row[posRow] == WORKING or row[posRow] == UKNOWN):
        if used == 0:
            res+= pd(posRow+1, posRules, 0, row, rules)
        elif used > 0 and posRules < len(rules) and rules[posRules] == used:
            res+= pd(posRow+1, posRules+1, 0, row, rules)
    if  (row[posRow] == DAMAGED or row[posRow] == UKNOWN):
        res+= pd(posRow+1, posRules, used+1, row, rules)
    dp[key] = res
    return res


res = 0
for l in sys.stdin:
    line = l.strip().split(' ')
    copies = []
    for i in range(5):
        copies.append(line[0])
   
    row = []
    for c in '?'.join(copies):
        row.append(c)

    rulesStr = line[1].split(',')*5
    rules = []
    for r in rulesStr:
        rules.append(int(r))
    dp.clear()
    calc = pd(0,0,0,row,rules)
    res+=calc
print (res)