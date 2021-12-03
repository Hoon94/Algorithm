import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

LOG = 21
N = int(input())
parent = [[0] * LOG for _ in range(N + 1)]
visit = [False] * (N + 1)
depth = [0] * (N + 1)
tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


def dfs(cur, d):
    visit[cur] = True
    depth[cur] = d
    for node in tree[cur]:
        if not visit[node]:
            parent[node][0] = cur
            dfs(node, d + 1)


def lca(a, b):
    if depth[a] > depth[b]:
        a, b = b, a

    for i in range(LOG - 1, -1, -1):
        if depth[b] - depth[a] >= (1 << i):
            b = parent[b][i]

    if a == b:
        return a

    for i in range(LOG - 1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    return parent[a][0]


dfs(1, 0)
for i in range(1, LOG):
    for j in range(1, N + 1):
        parent[j][i] = parent[parent[j][i - 1]][i - 1]

M = int(input())

for _ in range(M):
    a, b = map(int, input().split())
    print(lca(a, b))
