from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        N = len(nums)

        for i, num in enumerate(nums):
            for j in range(i + 1, N):
                if nums[j] == num:
                    return num
