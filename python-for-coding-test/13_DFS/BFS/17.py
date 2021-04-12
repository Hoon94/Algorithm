from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
s, X, Y = map(int, input().split())

move = [[-1, 0], [1, 0], [0, -1], [0, 1]]

q = []
for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            q.append([board[i][j], i, j, 0])

q.sort()
q = deque(q)

while q:
    virus, x, y, time = q.popleft()
    if time == s:
        break
    else:
        for dx, dy in move:
            if 0 <= x + dx < n and 0 <= y + dy < n and board[x + dx][y + dy] == 0:
                board[x + dx][y + dy] = virus
                q.append([virus, x + dx, y + dy, time + 1])

print(board[X - 1][Y - 1])
