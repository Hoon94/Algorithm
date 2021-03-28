from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """[summary]
        Given an array of integers nums sorted in ascending order,
        find the starting and ending position of a given target value.
        If target is not found in the array, return [-1, -1].

        Args:
            nums (List[int]): 0 <= nums.length <= 105, -109 <= nums[i] <= 109, nums is a non-decreasing array.
            target (int): -109 <= target <= 109

        Returns:
            List[int]: find the starting and ending position.

        Result:
            Runtime: 80 ms, faster than 89.04% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
            Memory Usage: 15.3 MB, less than 95.58% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.

        """

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start+end) // 2

            if nums[start] == nums[end] == target:
                return [start, end]

            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                if nums[start] != target:
                    start += 1
                if nums[end] != target:
                    end -= 1

        return [-1, -1]
