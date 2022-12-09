from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_start = 0
        min_size = float('inf')
        summation = 0

        for window_end, number in enumerate(nums):
            summation += number

            while summation >= target:
                min_size = min(min_size, window_end - window_start + 1)
                summation -= nums[window_start]
                window_start += 1

        if min_size == float('inf'):
            return 0
        else:
            return min_size
