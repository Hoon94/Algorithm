from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def helper(n):
            if n:
                helper(n - 1)
                ans.append([1] * n)

                for i in range(1, n - 1):
                    ans[n-1][i] = ans[n-2][i] + ans[n-2][i-1]

        ans = []
        helper(numRows)

        return ans
