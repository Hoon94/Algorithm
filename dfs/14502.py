from copy import deepcopy
import sys
sys.setrecursionlimit(1000)

N = M = 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y, arr):
    arr[x][y] = 2

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx and nx < N and 0 <= ny and ny < M:
            if arr[nx][ny] == 0:
                dfs(nx, ny, arr)

    #return arr

def getSafeArea(arr):
    safe = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                safe += 1
    
    return safe

#def setWall(start, depth):

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [[0] * M for _ in range(N)]

    for i in range(N):
        arr[i] = list(map(int, input().split()))

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                dfs(i, j, arr)