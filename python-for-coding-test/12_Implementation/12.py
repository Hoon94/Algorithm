def solution(n, build_frame):
    answer = [[]]
    board = [[0] * (n + 1) for _ in range(n + 1)]

    for frame in range(build_frame):
        x, y, a, b = frame.split()

        if a == 0:  # 기둥
            if b == 0:  # 삭제
                board[x][y] = 0
                board[x][y + 1] = 0
            else:  # 설치
                board[x][y] = 1
                board[x][y + 1] = 1

        else:  # 보
            if b == 0:  # 삭제
                board[x][y] = 0
                board[x + 1][y] = 0
            else:  # 설치
                board[x][y] = 1
                board[x + 1][y] = 1

    return answer


n = 5
build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [
    2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]

print(solution(n, build_frame))
