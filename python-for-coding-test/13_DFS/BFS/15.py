from collections import deque, defaultdict
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = defaultdict(list)
answer = []

for _ in range(m):
    start, end = map(int, input().split())
    graph[start] += [end]

queue = deque([(x, 0)])
visited = [x]

while queue:
    start, distance = queue.popleft()
    distance += 1
    for i in graph[start]:
        if i not in visited:
            if distance == k:
                answer.append(i)
                visited.append(i)
            else:
                queue.append((i, distance))
                visited.append(i)

if answer:
    for i in answer:
        print(i)
else:
    print(-1)
