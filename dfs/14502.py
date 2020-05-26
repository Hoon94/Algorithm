from copy import deepcopy

N = M = 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
virusList = []
result = 0

def dfs(x, y, arr):

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx and nx < N and 0 <= ny and ny < M:
            if arr[nx][ny] == 0:
                arr[nx][ny] = 2
                dfs(nx, ny, arr)

def getSafeArea(arr):
    safe = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                safe += 1
    
    return safe

def setWall(start, cnt, arr):
    global result
    wall = deepcopy(arr)

    if cnt == 3:
        for i in virusList:
            dfs(i[0], i[1], wall)

        result = max(result, getSafeArea(wall))
        #cnt = 0
        return

    for i in range(start, N*M):
        x = (int)(i / M)
        y = (int)(i % M)

        if wall[x][y] == 0:
            wall[x][y] = 1
            setWall(i + 1, cnt + 1, wall)
            wall[x][y] = 0


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [[0] * M for _ in range(N)]

    for i in range(N):
        arr[i] = list(map(int, input().split()))

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                virusList.append([i, j])

    setWall(0, 0, arr)
    print(result)