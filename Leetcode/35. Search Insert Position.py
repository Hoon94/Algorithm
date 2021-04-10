from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """[summary]
        Given a sorted array of distinct integers and a target value, return the index if the target is found.
        If not, return the index where it would be if it were inserted in order.

        Args:
            nums (List[int]): 1 <= nums.length <= 10 ** 4, -10 ** 4 <= nums[i] <= 10 ** 4, nums contains distinct values sorted in ascending order.
            target (int): -10 ** 4 <= target <= 10 ** 4

        Returns:
            int: Index if the target is found.

        Result:
            Runtime: 60 ms, faster than 6.10% of Python3 online submissions for Search Insert Position.
            Memory Usage: 14.9 MB, less than 79.30% of Python3 online submissions for Search Insert Position.
        """

        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
