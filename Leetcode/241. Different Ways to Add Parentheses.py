from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def helper(l, r):
            ans = []

            for i in range(l, r):
                if expression[i] not in ops:
                    continue
                ans += [ops[expression[i]](le, ri) for le in helper(l, i)
                        for ri in helper(i + 1, r)]

            return ans if len(ans) != 0 else [int(expression[l:r])]

        ops = {
            '-': lambda x, y: x - y,
            '+': lambda x, y: x + y,
            '*': lambda x, y: x * y,
        }

        return helper(0, len(expression))
