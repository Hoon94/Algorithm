from copy import deepcopy
import sys
sys.setrecursionlimit(1000)

def dfs(x, y, arr):
    arr[x][y] = 2

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        
        if arr[nx][ny] == 0:
            dfs(nx, ny, arr)

    return arr


N, M = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

arr = [[0] * M for _ in range(N)]

for i in range(N):
    arr[i] = list(map(int, input().split()))
    
i = 0
j = 0
while True:
    wall = deepcopy(arr)
    cnt = 0
    result = 0
    for i in range(N):
        for j in range(M):
            if wall[i][j] == 0:
                wall[i][j] = 1
                if cnt == 0:
                    a = i
                    b = j 
                cnt += 1
            
            if cnt == 3:
                wall = dfs(0, 0, wall)
                for k in range(N):
                    for l in range(M):
                        if wall[k][l] == 0:
                            result += 1
                break

print(result)           