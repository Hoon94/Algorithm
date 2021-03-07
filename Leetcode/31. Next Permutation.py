class Solution:
    def nextPermutation(self, nums):
        """[summary]
            Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
            If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
            The replacement must be in place and use only constant extra memory.

        Args:
            nums ([type]): 1 <= nums.length <= 100, 0 <= nums[i] <= 100

        Result:
            Runtime: 32 ms, faster than 99.08% of Python3 online submissions for Next Permutation.
            Memory Usage: 14.2 MB, less than 57.40% of Python3 online submissions for Next Permutation.
        """

        i = len(nums) - 1

        while i > 0:
            if nums[i - 1] < nums[i]:
                break
            i -= 1

        i -= 1
        j = len(nums) - 1

        while j > i:
            if nums[j] > nums[i]:
                break
            j -= 1

        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = sorted(nums[i + 1:])
