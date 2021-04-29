from collections import deque


def can_move(p1, p2, new_board):
    y, x = 0, 1
    cand = []
    # 평행이동
    move = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for dy, dx in move:
        nxt1 = (p1[y] + dy, p1[x] + dx)
        nxt2 = (p2[y] + dy, p2[x] + dx)
        if new_board[nxt1[y]][nxt1[x]] == 0 and new_board[nxt2[y]][nxt2[x]] == 0:
            cand.append((nxt1, nxt2))

    # 회전
    if p1[y] == p2[y]:  # 가로 방향 일 때
        up, down = -1, 1
        for d in [up, down]:
            if new_board[p1[y] + d][p1[x]] == 0 and new_board[p2[y] + d][p2[x]] == 0:
                cand.append((p1, (p1[y] + d, p1[x])))
                cand.append((p2, (p2[y] + d, p2[x])))
    else:  # 세로 방향 일 때
        left, right = -1, 1
        for d in [left, right]:
            if new_board[p1[y]][p1[x] + d] == 0 and new_board[p2[y]][p2[x] + d] == 0:
                cand.append(((p1[y], p1[x] + d), p1))
                cand.append(((p2[y], p2[x] + d), p2))

    return cand


def solution(board):
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    print(new_board)
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    q = deque([((1, 1), (1, 2), 0)])
    visited = set([((1, 1), (1, 2))])

    while q:
        p1, p2, count = q.popleft()
        if p1 == (n, n) or p2 == (n, n):
            return count
        for nxt in can_move(p1, p2, new_board):
            if nxt not in visited:
                q.append((*nxt, count + 1))
                visited.add(nxt)
