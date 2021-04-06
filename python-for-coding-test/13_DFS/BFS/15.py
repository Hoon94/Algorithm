from collections import deque, defaultdict
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    start, end = map(int, input().split())
    graph[start] += [end]

queue = deque([x])
distance = [-1] * (n + 1)
distance[x] = 0

while queue:
    start = queue.popleft()
    for i in graph[start]:
        if distance[i] == -1:
            distance[i] = distance[start] + 1
            queue.append(i)

check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)
