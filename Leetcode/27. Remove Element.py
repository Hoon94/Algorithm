from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """[summary]
        Given an array nums and a value val, remove all instances of that value in-place and return the new length.
        Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
        The order of elements can be changed. It doesn't matter what you leave beyond the new length.

        Clarification:
        Confused why the returned value is an integer but your answer is an array?
        Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.

        Args:
            nums (List[int]): 0 <= nums.length <= 100, 0 <= nums[i] <= 50
            val (int): 0 <= val <= 100

        Returns:
            int: return the new length.

        Result:
            Runtime: 32 ms, faster than 78.11% of Python3 online submissions for Remove Element.
            Memory Usage: 14.2 MB, less than 49.40% of Python3 online submissions for Remove Element.
        """

        for i in range(nums.count(val)):
            nums.remove(val)

        return len(nums)
