import sys
import random
def bfs(graph, s, t, parent):
    visited = {}
    queue = []
    queue.append(s)
    visited[s] = True
    parent[s] = -1
    while(len(queue) > 0):
        u = queue.pop()
        for v in graph[u]:
            if v not in visited and graph[u][v] > 0:
                queue.append(v)
                parent[v] = u
                visited[v] = True
    return t in visited

def dfs(graph, s, visited):
    visited[s] = True
    for v in graph[s]:
        if (graph[s][v] > 0 and v not in visited):
            dfs(graph, v, visited)

def minCut(graph, s, t):
    rGraph = {}
    for u in graph:
        rGraph[u] = {}
        for v in graph[u]:
            rGraph[u][v] = 1
    parent = {}
    while( bfs(rGraph, s, t, parent)):
        pathFlow = -1
        v = t
        while(v != s):
            u = parent[v]
            if (pathFlow == -1):
                pathFlow = rGraph[u][v]
            pathFlow = min(pathFlow, rGraph[u][v])
            v = u
        
        v = t
        while(v != s):
            u = parent[v]
            rGraph[u][v] -= pathFlow
            rGraph[v][u] += pathFlow
            v = u
    
    visited = {}
    dfs(rGraph, s, visited)
    res = []
    for i in graph:
        for j in graph[i]:
            if i in visited and j not in visited:
                res.append((i,j))
    return (res, len(visited))



graph = {}
for line in sys.stdin:
    line = line.strip()
    src, dsts = line.split(':')
    if src not in graph:
        graph[src] = {}
    for dst in dsts.strip().split(' '):
        if dst not in graph:
            graph[dst] = {}
        graph[src][dst] = 1
        graph[dst][src] = 1

s = random.choice(list(graph.keys()))
t = random.choice(list(graph.keys()))
while(t == s):
    t = random.choice(list(graph.keys()))
x, count = minCut(graph,s,t )
while(len(x) > 3):
    s = random.choice(list(graph.keys()))
    t = random.choice(list(graph.keys()))
    while(t == s):
        t = random.choice(list(graph.keys()))
    x, count = minCut(graph,s,t )
count2 = len(graph) - count
print(count * count2)