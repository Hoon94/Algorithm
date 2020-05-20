from collections import deque

a = deque()
a.append([1, 2])
x, y = a.popleft()

print(x)
print(y)