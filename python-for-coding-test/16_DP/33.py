N = int(input())
T = []
P = []
for i in range(N):
    a, b = map(int, input().split(' '))
    T.append(a)
    P.append(b)

dp = [0 for _ in range(N + 2)]

for i in range(N):
    if dp[i] > dp[i + 1]:
        dp[i + 1] = dp[i]

    if i + T[i] <= N:
        if dp[i + T[i]] < P[i] + dp[i]:
            dp[i + T[i]] = P[i] + dp[i]

ans = 0
if dp[N] > dp[N - 1]:
    ans = dp[N]
else:
    ans = dp[N - 1]
print(dp)


# import sys

# n = int(input())
# timeTable = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# dp = [0 for _ in range(n + 1)]

# for i in range(n - 1, -1, -1):
#     if i + timeTable[i][0] > n:
#         dp[i] = dp[i + 1]
#     else:
#         dp[i] = max(timeTable[i][1] + dp[i + timeTable[i][0]], dp[i + 1])

# print(dp[0])
