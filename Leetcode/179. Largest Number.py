from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not any(nums):
            return "0"

        return "".join(sorted(map(str, nums), cmp=lambda n1, n2: -1 if n1 + n2 > n2 + n1 else (1 if n1 + n2 < n2 + n1 else 0)))
