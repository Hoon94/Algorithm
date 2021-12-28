import sys
sys.setrecursionlimit(100000)


def go(idx, left):
    if idx == n:
        return 0
    if dp[idx][left] != -1:
        return dp[idx][left]
    dp[idx][left] = 9876543210

    if left:
        now = (arr[idx] + left) % 10
    else:
        now = arr[idx]

    dp[idx][left] = min(dp[idx][left], go(
        idx + 1, (left + left_cache[now][res[idx]]) % 10) + left_cache[now][res[idx]])
    dp[idx][left] = min(dp[idx][left], go(
        idx + 1, left) + right_cache[now][res[idx]])

    return dp[idx][left]


left_cache = [[-1] * 10 for _ in range(10)]
right_cache = [[-1] * 10 for _ in range(10)]

for i in range(10):
    for j in range(10):
        temp = 0

        while True:
            if (i + temp) % 10 == j:
                break
            temp += 1

        left_cache[i][j] = temp
        temp = 0

        while True:
            if (i - temp) % 10 == j:
                break
            temp += 1

        right_cache[i][j] = temp

n = int(sys.stdin.readline())
dp = [[-1] * 10 for _ in range(n)]
arr = list(map(int, sys.stdin.readline().rstrip()))
res = list(map(int, sys.stdin.readline().rstrip()))

print(go(0, 0))
