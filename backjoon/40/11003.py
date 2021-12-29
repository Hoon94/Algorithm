import sys
from collections import deque

n, l = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
d = [0 for _ in range(n)]
window = deque()

for idx in range(n):
    while window and window[-1][1] > arr[idx]:
        window.pop()

    while window and idx - window[0][0] >= l:
        window.popleft()

    window.append((idx, arr[idx]))
    d[idx] = window[0][1]

print(*d)
