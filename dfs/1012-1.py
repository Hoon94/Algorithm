import sys
sys.setrecursionlimit(11)
#Python의 경우 최대 재귀 깊이는 1000으로 설정되어있다.

def dfs(x, y):
    answer.append([x, y])
    arr[x][y] = 0
    global cnt

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        
        if arr[nx][ny]:
            cnt += 1
            dfs(nx, ny)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
answer = []
M, N= map(int, input().split())
cnt = 0
arr = [[1] * M for _ in range(N)]

for j in range(N):
    for k in range(M):
        if arr[j][k]:
            cnt += 1
            dfs(j, k)

print(answer)
print(len(answer))