from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(k):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        return nums[len(nums) - k]
