from collections import deque
import sys
input = sys.stdin.readline

n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(row, col):
    check = False
    visited = {(row, col)}
    q = deque([(row, col)])
    val, cnt = 0, 0

    while q:
        x, y = q.popleft()
        val += arr[x][y]
        cnt += 1
        for i in range(4):
            nx = x + dy[i]
            ny = y + dx[i]

            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited and l <= abs(arr[nx][ny] - arr[x][y]) <= r:
                q.append((nx, ny))
                visited.add((nx, ny))
                check = True
    return val // cnt, visited, check


def move():
    cnt = 0
    while True:
        is_move = False
        total_visited = set()
        temp = []
        for i in range(n):
            for j in range(n):
                if (i, j) not in total_visited:
                    value, visited, flag = bfs(i, j)
                    if flag:
                        is_move = True
                    temp.append((value, visited))
                    total_visited |= visited

        for (value, visit) in temp:
            for y, x in visit:
                arr[y][x] = value
        if not is_move:
            return cnt
        cnt += 1


print(move())
