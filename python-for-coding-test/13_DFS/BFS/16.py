def dfs(x, y, arr):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx and nx < n and 0 <= ny and ny < m:
            if arr[nx][ny] == 0:
                arr[nx][ny] = 2
                dfs(nx, ny, arr)


def getSafeArea(arr):
    safe = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                safe += 1

    return safe


def setWall(start, cnt, arr):
    global result

    if cnt == 3:
        for i in virusList:
            dfs(i[0], i[1], arr)

        result = max(result, getSafeArea(arr))
        return

    for i in range(start, n * m):
        x = i // m
        y = i % m

        if arr[x][y] == 0:
            arr[x][y] = 1
            setWall(i + 1, cnt + 1, arr)
            arr[x][y] = 0


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
virusList = []
result = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            virusList.append([i, j])

setWall(0, 0, arr)
print(result)
