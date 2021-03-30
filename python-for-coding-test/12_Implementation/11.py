from collections import deque


def check(x, y):
    if 0 <= x and x < n and 0 <= y and y < n:
        return True

    return False


def turn_around(direction):
    global d
    if direction == 'D':
        d = (d + 1) % 4
    else:
        d = (d - 1) % 4
    return d


n = int(input())
k = int(input())
board = [[0 for x in range(n)] for y in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1

l = int(input())
step = dict()
for _ in range(l):
    time, direction = input().split()
    step[int(time)] = direction

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

snake = deque([[0, 0]])

d = 0
times = 0
nx, ny = 0, 0

while True:
    times += 1
    nx += dx[d]
    ny += dy[d]

    if times in step.keys():
        d = turn_around(step[times])

    if check(nx, ny):
        if [nx, ny] in snake:
            break

        if board[nx][ny] == 1:
            board[nx][ny] = 0
            snake.append([nx, ny])

        elif board[nx][ny] == 0:
            snake.append([nx, ny])
            x, y = snake.popleft()
    else:
        break

print(times)
