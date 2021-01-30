class Solution(object):
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        dp = [1] + [0] * n
        prev = dp[:]

        for i in range(len(p)):
            pprev = prev
            prev = dp
            dp = [0] * (n + 1)
            if p[i] == '*':
                for j in range(n + 1):
                    if pprev[j]:
                        dp[j] = 1
                        k = j + 1
                        while k < n + 1 and p[i - 1] in ('.', s[k - 1]):
                            dp[k] = 1
                            k += 1
            else:
                for j in range(n):
                    if prev[j]:
                        dp[j + 1] = p[i] in ('.', s[j])

        return dp[-1]
