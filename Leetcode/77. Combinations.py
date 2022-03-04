from typing import List
from functools import reduce


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return reduce(lambda C, _: [[i] + c for c in C for i in range(1, c[0] if c else n + 1)], range(k), [[]])
