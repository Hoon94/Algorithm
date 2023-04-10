from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        N = len(nums) - 1
        lo, hi = 1, N

        while lo < hi:
            mi = (lo + hi) >> 1
            less, equal = 0, 0

            for num in nums:
                if num < mi:
                    less += 1
                elif num == mi:
                    equal += 1

            if equal > 1:
                return mi

            if less >= mi:
                hi = mi - 1
            else:
                lo = mi + 1

        return lo
