import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())

adj = [[0 for i in range(N + 1)] for j in range(N + 1)]

#print(adj)

for i in range(M):
    a, b = map(int, input().split())
    adj[a][b] = 1
    adj[b][a] = 1

def dfs(V, hist, adj):
    hist.append(V)
    for i in range(1, N + 1):
        if adj[V][i] and i not in hist:
            hist = dfs(i, hist, adj)
    return hist

def bfs(V, adj):
    q = [V]
    hist = [V]
    while q:
        now = q.pop(0)
        for i in range(1, N + 1):
            if adj[now][i] and i not in hist:
                q.append(i)
                hist.append(i)
    return hist


print(*dfs(V, [], adj))
print(*bfs(V, adj))


'''
from collections import deque 

def bfs(graph, start): 
    for i in graph: 
        graph[i].sort() 
        
    explored, queue = set(), deque([start]) 
    explored.add(start) 
    track_list = [start] 
    while queue: 
        v = queue.popleft() # queue.popleft() 
        if v in graph: 
            for w in graph[v]: 
                if w not in explored: 
                    explored.add(w) 
                    track_list.append(w) 
                    queue.append(w) 
                    
    return track_list 
        
def dfs(graph, start): 
    for i in graph: 
        graph[i].sort(reverse=True) 
        
    track_list, explored, stack = list(), set(), deque([start]) 
        
    while stack: 
        v = stack.pop() # one difference from BFS is to pop last element here instead of first one 
            
        if v in explored: 
            continue 
            
        explored.add(v) 
        track_list.append(v) 
            
        if v in graph: 
            for w in graph[v]: 
                if w not in explored: 
                    stack.append(w) 
                        
    return track_list 
    
n, m, v = map(int, input().split()) 
graph = {} 

for _ in range(m): 
    a, b = map(int, input().split()) 
    if a in graph:
        graph[a].append(b) 
    else: 
        graph[a] = [b] 
    
    if b in graph: 
        graph[b].append(a) 
    else: 
        graph[b] = [a] 
        
print(*dfs(graph, v)) 
print(*bfs(graph, v))

#printing the list using * operator separated by space
#print(*list, sep = '')
'''