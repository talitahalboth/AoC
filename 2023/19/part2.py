pos = {'x': 0, 'm': 1, 'a': 2, 's': 3}
workflow = input()
adj = {}
while (len(workflow) > 0):
    workflowName = workflow.split('{')[0]
    rules = workflow.split('{')[1].split('}')[0].split(',')
    ranges = []
    for i in range(0,4):
        ranges.append([0, 4001])
    for rule in rules:
        if (':' in rule):
            dest = rule.split(':')[1]
            cleanRule = rule.split(':')[0]
            splitRule = cleanRule.split('<') if ('<' in cleanRule) else cleanRule.split('>')
            cat = splitRule[0]
            val = int(splitRule[1])
            res = []
            for pair in ranges:
                res.append(pair.copy())
            if ('<' in cleanRule):
                res[pos[cat]][1] = min(res[pos[cat]][1], val)
                ranges[pos[cat]][0] = max(ranges[pos[cat]][0], val- 1)
            else:
                res[pos[cat]][0] = max(res[pos[cat]][0], val)
                ranges[pos[cat]][1] = min(ranges[pos[cat]][1], val+1)
            if (dest not in adj):
                adj[dest] = []
            adj[dest].append([workflowName, res.copy()])
        else:
            dest = rule
            if (dest not in adj):
                adj[dest] = []
            adj[dest].append([workflowName, ranges.copy()])
    workflow = input()

def dfs(node, path, res):
    if node[0] == "in":
        newPath = path.copy()
        newPath.append(node)
        res.append(newPath)
        return
    path.append(node)
    for newNode in adj[node[0]]:
        dfs(newNode, path, res )
    path.pop()
    return 
paths = []
for node in adj['A']:
    dfs(node, [], paths)
res = 0
for path in paths:
    ranges = path[0][1]
    for elem in path:
        for index, range in enumerate(elem[1]):
            ranges[index][0] = max(range[0], ranges[index][0])
            ranges[index][1] = min(range[1], ranges[index][1])
    tmp = 1
    for range in ranges:
        tmp*=range[1] - range[0] - 1
    res+=tmp
print(res)