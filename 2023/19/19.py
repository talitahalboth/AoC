import sys

pos = {'x': 0, 'm': 1, 'a': 2, 's': 3}
workflow = input()
workflows = {}
while (len(workflow) > 0):
    workflowName = workflow.split('{')[0]
    rules = workflow.split('{')[1].split('}')[0].split(',')
    workflows[workflowName] = rules
    workflow = input()

def compareRule(rule,rate):
    splitRule = rule.split('<') if ('<' in rule) else rule.split('>')
    cat = splitRule[0]
    val = splitRule[1].split(':')[0]
    nextRule =  splitRule[1].split(':')[1]
    if ('<' in rule and int(rate[pos[cat]]) < int(val)) or ('>' in rule and int(rate[pos[cat]]) > int(val)):
        return nextRule
    return "in"

res = 0        
for line in sys.stdin:
    line = line.strip()[1:-1].split(',')
    rates = []
    for i in range(0,4):
        rates.append(int(line[i].split('=')[1]))
    isEnd = False
    nextRule = "in"
    while (not isEnd):
        rules = workflows[nextRule]
        nextRule = "in"
        for rule in rules:
            if (nextRule == "in"):
                if (':' in rule):
                    nextRule = compareRule(rule,rates)
                else:
                    nextRule = rule
        if (nextRule == "A" or nextRule == "R"):
            isEnd = True
    if (nextRule == "A"):
        res = res + sum(rates)
print(res)