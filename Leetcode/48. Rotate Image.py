from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n / 2):
            for j in range(n - n / 2):
                for _ in '123':
                    matrix[i][j], matrix[~j][i], i, j = matrix[~j][i], matrix[i][j], ~j, ~i
                i = ~j
