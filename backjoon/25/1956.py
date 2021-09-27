import sys

v, e = map(int, sys.stdin.readline().split())
INF = 100000000
result = INF
s = [[INF] * v for _ in range(v)]

for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    s[a - 1][b - 1] = c

for k in range(v):
    for i in range(v):
        for j in range(v):
            if s[i][j] > s[i][k] + s[k][j]:
                s[i][j] = s[i][k] + s[k][j]

for i in range(v):
    result = min(result, s[i][i])

if result == INF:
    print(-1)
else:
    print(result)
