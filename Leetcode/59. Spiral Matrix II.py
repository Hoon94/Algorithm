from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        A, lo = [], n * n + 1

        while lo > 1:
            lo, hi = lo - len(A), lo
            A = [range(lo, hi)] + zip(*A[::-1])

        return A
