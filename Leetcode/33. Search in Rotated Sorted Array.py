from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """[summary]
        There is an integer array nums sorted in ascending order (with distinct values).
        Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length)
        such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
        For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
        Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

        Args:
            nums (List[int]): 1 <= nums.length <= 5000, -104 <= nums[i] <= 104, All values of nums are unique, nums is guaranteed to be rotated at some pivot.
            target (int): -104 <= target <= 104

        Returns:
            int: Index of target

        Result:
            Runtime: 40 ms, faster than 76.50% of Python3 online submissions for Search in Rotated Sorted Array.
            Memory Usage: 14.8 MB, less than 24.17% of Python3 online submissions for Search in Rotated Sorted Array.
        """

        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1
