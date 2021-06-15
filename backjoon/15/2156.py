n = int(input())
wine = [0]
dp = [0]
[wine.append(int(input())) for _ in range(n)]
dp.append(wine[1])

if n > 1:
    dp.append(wine[1] + wine[2])

for i in range(3, n + 1):
    case1 = wine[i] + dp[i - 2]
    case2 = wine[i] + wine[i - 1] + dp[i - 3]
    case3 = dp[i - 1]
    dp.append(max(case1, case2, case3))

print(dp[n])
