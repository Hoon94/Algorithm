from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """[summary]

        Args:
            nums (List[int]): [description]
            target (int): [description]

        Returns:
            int: [description]

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
