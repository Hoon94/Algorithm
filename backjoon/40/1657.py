import sys

# 재귀깊이해제
sys.setrecursionlimit(10000)

# 입력부
n, m = map(int, sys.stdin.readline().split())
tofu = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

# cost : 두부 비용을 담는 2차원 딕셔너리
cost = dict().fromkeys(['A', 'B', 'C', 'D', 'F'])
for i in cost:
    cost[i] = dict().fromkeys(['A', 'B', 'C', 'D', 'F'], 0)
temp = [[10, 8, 7, 5, 1], [8, 6, 4, 3, 1], [
    7, 4, 3, 2, 1], [5, 3, 2, 2, 1], [1, 1, 1, 1, 0]]
for idx_i, i in enumerate(['A', 'B', 'C', 'D', 'F']):
    for idx_j, j in enumerate(['A', 'B', 'C', 'D', 'F']):
        cost[i][j] = temp[idx_i][idx_j]

# dp : 현재 i번째 칸에서 j번째 비트일 때 얻을 수 있는 두부 가격의 최대값
dp = [[-1] * (1 << m) for _ in range(n * m)]


def go(num, bit):
    # 범위를 초과하는 경우 불가능하므로 0리턴
    if num >= n * m:
        return 0

    # Memoization
    if dp[num][bit] != -1:
        return dp[num][bit]
    dp[num][bit] = 0

    # d : 현재 비트가 있든 없든 해당 칸을 그냥 지나치는 경우 얻을 수 있는 두부 가격
    d = go(num + 1, bit >> 1)

    # 현재 값과 d 비교
    dp[num][bit] = max(dp[num][bit], d)

    # 현재 비트가 채워져 있으면 넘어간다
    if bit & 1 == 1:
        # a : 현재 비트가 있어서 해당 칸을 그냥 지나치는 경우 얻을 수 있는 두부 가격
        a = go(num + 1, bit >> 1)
        # 현재 값과 a 비교
        dp[num][bit] = max(dp[num][bit], a)

    # 현재 비트가 안 채워져 있으면 옆 또는 밑칸을 채운다
    else:
        # 밑칸이 범위를 벗어나지 않는 경우
        if num + m < n * m and bit & 1 == 0:
            # b : 현재 비트가 없어서 해당 칸과 밑칸을 한 덩이로 자를 때 얻을 수 있는 두부 가격
            b = go(num + 1, bit >> 1 | (1 << (m - 1)))
            # 현재 값과 비교
            dp[num][bit] = max(dp[num][bit], b +
                               cost[one_dim[num]][one_dim[num + m]])

        # 옆칸이 범위를 벗어나지 않는 경우
        if num % m != (m - 1) and bit & 2 == 0:
            # c : 현재 비트가 없어서 해당 칸과 옆칸을 한 덩이로 자를 때 얻을 수 있는 두부 가격
            c = go(num + 2, bit >> 2)
            # 현재 값과 비교
            dp[num][bit] = max(dp[num][bit], c +
                               cost[one_dim[num]][one_dim[num + 1]])
    return dp[num][bit]


# 정답 출력
print(go(0, 0))
