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

print(graph)
print(graph[1])