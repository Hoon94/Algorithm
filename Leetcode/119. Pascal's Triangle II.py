from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1] * (rowIndex + 1)
        up = rowIndex
        down = 1

        for i in range(1, rowIndex):
            ans[i] = ans[i - 1] * up / down
            up -= up
            down += down

        return ans
