n = int(input())
board = []
teachers = []
obstacle = []
result = "NO"
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for i in range(n):
    board.append(input().split())
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i, j))


def check():
    for teacher in teachers:
        for i in range(4):
            x, y = teacher
            while 0 <= x < n and 0 <= y < n:
                if board[x][y] == 'O':
                    break
                elif board[x][y] == 'S':
                    return False
                x += move[i][0]
                y += move[i][1]
    return True


def dfs(count):
    global result
    if count > 3:
        return
    if count == 3:
        if check():
            result = "YES"
            return
        else:
            result = "NO"

    for i in range(n):
        for j in range(n):
            if board[i][j] == 'X':
                board[i][j] = 'O'
                dfs(count + 1)
                if result == "YES":
                    return
                board[i][j] = 'X'


dfs(0)
print(result)
