import sys
read = sys.stdin.readline

for _ in range(int(read())):
    n = int(read())
    num = list(map(int, read().split()))
    dp = list(list(0 for _ in range(n)) for _ in range(n))

    for k in range(1, n):
        for i in range(n - k):
            X, Y = i, i + k
            dp[X][Y] = 2147000000

            for j in range(k):
                tmp = dp[X + 1 + j][Y] + dp[X][Y - k + j]
                dp[X][Y] = min(dp[X][Y], tmp)

            dp[X][Y] += sum(num[X:Y + 1])

    print(dp[0][-1])
