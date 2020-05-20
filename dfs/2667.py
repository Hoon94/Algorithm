def dfs(x, y, arr):
    arr[x][y] = 0
    cnt = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if arr[nx][ny]:
            cnt += dfs(nx, ny, arr)

    return cnt

N = int(input())

arr = [[0] * N for i in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
apt = []

for i in range(N):
    arr[i] = list(map(int, input()))

for i in range(N):
    for j in range(N):
        if arr[i][j]:
            apt.append(dfs(i, j, arr))

print(len(apt))
apt.sort()
for i in apt:
    print(i)