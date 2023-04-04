from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        if not num:
            return []

        num_len = len(num)
        res = []

        def dfs(idx, path):
            if idx == num_len - 1:
                path = path + num[idx]

                if eval(path) == target:
                    res.append(path)

                return

            dfs(idx + 1, path + num[idx] + "+")
            dfs(idx + 1, path + num[idx] + "-")
            dfs(idx + 1, path + num[idx] + "*")

            if (path and path[-1] not in ['+', '-', '*'] and num[idx] == '0') or num[idx] != '0':
                dfs(idx + 1, path + num[idx])

        dfs(0, "")

        return res
