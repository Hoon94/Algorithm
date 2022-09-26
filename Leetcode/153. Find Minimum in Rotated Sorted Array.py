from typing import List
import bisect


class Solution:
    def findMin(self, nums: List[int]) -> int:
        self.__getitem__ = lambda i: nums[i] <= nums[-1]
        return nums[bisect.bisect(self, False, 0, len(nums))]
