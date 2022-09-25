from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        current = 1

        for i in nums:
            current *= i
            ans = max(ans, current)

            if current == 0:
                current = 1

        current = 1

        for i in reversed(nums):
            current *= i
            ans = max(ans, current)

            if current == 0:
                current = 1

        return ans
