from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = {}

        for n in nums:
            if m[n] > len(nums) // 2:
                return n

            m[n] = m.get(n, 0) + 1
