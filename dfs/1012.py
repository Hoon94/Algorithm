def dfs(x, y, arr):
    arr[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        
        if arr[nx][ny]:
            dfs(nx, ny, arr)

T = int(input())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
answer = []

for i in range(T):
    M, N, K = map(int, input().split())
    cnt = 0
    arr = [[0] * M for _ in range(N)]

    for j in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1

    for j in range(N):
        for k in range(M):
            if arr[j][k]:
                dfs(j, k, arr)
                cnt += 1

    answer.append(cnt)

for i in answer:
    print(i)