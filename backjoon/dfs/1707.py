from collections import deque
import sys


def bfs(start):
    bi[start] = 1
    q = deque()
    q.append(start)

    while q:
        a = q.popleft()
        for i in s[a]:
            if bi[i] == 0:
                bi[i] = -bi[a]
                q.append(i)
            else:
                if bi[i] == bi[a]:
                    return False

    return True


input = sys.stdin.readline
k = int(input())

for i in range(k):
    v, e = map(int, input().split())
    isTrue = True
    s = [[] for _ in range(v + 1)]
    bi = [0 for _ in range(v + 1)]

    for j in range(e):
        a, b = map(int, input().split())
        s[a].append(b)
        s[b].append(a)

    for k in range(1, v + 1):
        if bi[k] == 0:
            if not bfs(k):
                isTrue = False
                break

    print("YES" if isTrue else "NO")
