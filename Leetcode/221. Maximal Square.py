from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        for i, r in enumerate(matrix):
            r = matrix[i] = map(int, r)
            for j, c in enumerate(r):
                if i * j * c:
                    r[j] = min(matrix[i - 1][j], r[j - 1],
                               matrix[i - 1][j - 1]) + 1

        return max(map(max, matrix + [[0]])) ** 2
