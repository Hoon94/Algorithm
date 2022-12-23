from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums), len(nums) - k, -1):
            tmp = 0

            for j in range(i):
                if nums[j] > nums[tmp]:
                    tmp = j

            nums[tmp], nums[i - 1] = nums[i - 1], nums[tmp]

        return nums[len(nums) - k]
