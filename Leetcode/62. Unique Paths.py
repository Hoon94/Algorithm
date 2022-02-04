from math import factorial


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows, cols = m, n

        return factorial(rows + cols - 2) // (factorial(rows - 1) * factorial(cols - 1))
