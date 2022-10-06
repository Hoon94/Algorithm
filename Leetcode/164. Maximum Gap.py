from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        nums = [bin(num)[2:][::-1] for num in nums]

        for i in range(max(map(len, nums))):
            nums0 = [x for x in nums if i >= len(x) or x[i] == '0']
            nums1 = [x for x in nums if i < len(x) and x[i] == '1']
            nums = nums0 + nums1

        nums = [int(num[::-1], 2) for num in nums]

        return max(nums[i] - nums[i - 1] for i in range(1, len(nums)))
