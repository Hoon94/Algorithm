from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            if nums[abs(num)] < 0:
                ans = abs(num)
                break

            nums[abs(num)] = -nums[abs(num)]

        for i in range(len(nums)):
            nums[i] = abs(nums[i])

        return ans
