from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """[summary]
            Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
            Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

            Clarification:
            Confused why the returned value is an integer but your answer is an array?
            Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.

        Args:
            nums (List[int]): 0 <= nums.length <= 3 * 104, -104 <= nums[i] <= 104, nums is sorted in ascending order.

        Returns:
            int: returns the new length.

        Result:
            Runtime: 76 ms, faster than 92.95% of Python3 online submissions for Remove Duplicates from Sorted Array.
            Memory Usage: 16.2 MB, less than 11.09% of Python3 online submissions for Remove Duplicates from Sorted Array.
        """

        nums[:] = sorted(set(nums))

        return len(nums)
