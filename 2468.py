n = int(input())
s = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
max_cnt = 0

def bfs(j, k):
    queue = [[j, k]]
    
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < n and 0 <= y < n and copy[x][y] == 0:
                copy[x][y] = 1
                queue.append([x, y])

for i in range(n):
    a = list(map(int, input().split()))
    s.append(a)

for i in range(0, 101):
    copy = [[0] * n for i in range(n)]
    cnt = 0

    for j in range(n):
        for k in range(n):
            if s[j][k] <= i:
                copy[j][k] = 1
    
    for j in range(n):
        for k in range(n):
            if copy[j][k] == 0:
                copy[j][k] = 1
                bfs(j, k)
                cnt += 1
    
    if cnt == 0:
        break
    
    max_cnt = max(max_cnt, cnt)

print(max_cnt)