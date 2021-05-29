import sys

n = int(input())
timeTable = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [0 for _ in range(n + 1)]

for i in range(n - 1, -1, -1):
    if i + timeTable[i][0] > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(timeTable[i][1] + dp[i + timeTable[i][0]], dp[i + 1])

print(dp[0])
