from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        area = 0
        if matrix:
            p = [0] * len(matrix[0])
            for row in matrix:
                s = map(int, row)
                for j, c in enumerate(s[1:], 1):
                    s[j] *= min(p[j - 1], p[j], s[j - 1]) + 1
                area = max(area, max(s) ** 2)
                p = s

        return area
