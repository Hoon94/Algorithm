import sys
input = sys.stdin.readline


def dfs(prev, node):
    visited[node] = True
    for n in graph[node]:
        if n == prev:
            continue
        if visited[n]:
            return False
        if not dfs(node, n):
            return False
    return True


tc = 0
while True:
    tc += 1
    N, M = map(int, input().split())
    if [N, M] == [0, 0]:
        break
    graph = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    cnt = 0
    for v in range(1, N + 1):
        if not visited[v]:
            if dfs(0, v):
                cnt += 1
    if cnt == 0:
        print("Case {}: No trees.".format(tc))
    elif cnt == 1:
        print("Case {}: There is one tree.".format(tc))
    else:
        print("Case {}: A forest of {} trees.".format(tc, cnt))
