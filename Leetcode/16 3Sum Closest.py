class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        """[summary]
        Given an array nums of n integers and an integer target,
        find three integers in nums such that the sum is closest to target.
        Return the sum of the three integers.
        You may assume that each input would have exactly one solution.

        Args:
            nums (List[int]): 3 <= nums.length <= 10^3, -10^3 <= nums[i] <= 10^3
            target (int): -10^4 <= target <= 10^4

        Returns:
            int: The sum that is closest to the target.
        """

        res = 10 ** 4 + 1
        nums.sort()
        n = len(nums)

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                closest = sum([nums[i], nums[left], nums[right]])
                diff = closest - target

                if abs(diff) < res:
                    out = [nums[i], nums[left], nums[right]]
                    res = abs(diff)

                if diff == 0:
                    return sum(out)
                elif diff > 0:
                    right -= 1
                elif diff < 0:
                    left += 1

        return sum(out)
