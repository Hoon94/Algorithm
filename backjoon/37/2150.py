import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
reverse_graph = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    reverse_graph[b].append(a)


def dfs(node, visit, stack):
    visit[node] = 1
    for now in graph[node]:
        if visit[now] == 0:
            dfs(now, visit, stack)
    stack.append(node)


def reverse_dfs(node, visit, stack):
    visit[node] = 1
    stack.append(node)
    for now in reverse_graph[node]:
        if visit[now] == 0:
            reverse_dfs(now, visit, stack)


stack = []
visit = [0] * (V + 1)

for i in range(1, V + 1):
    if visit[i] == 0:
        dfs(i, visit, stack)
visit = [0] * (V + 1)
result = []

while stack:
    ssc = []
    node = stack.pop()
    if visit[node] == 0:
        reverse_dfs(node, visit, ssc)
        result.append(sorted(ssc))

print(len(result))
answer = sorted(result)
for i in answer:
    print(*i, -1)
