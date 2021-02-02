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

        Result:
            Runtime: 140 ms, faster than 49.68% of Python3 online submissions for 3Sum Closest.
            Memory Usage: 14.2 MB, less than 90.96% of Python3 online submissions for 3Sum Closest.
        """

        current = float('inf')
        nums.sort()
        n = len(nums)

        for i in range(n - 2):
            low = i + 1
            high = n - 1

            while low < high:
                closest = sum([nums[i], nums[low], nums[high]])
                diff = closest - target

                if abs(diff) < current:
                    res = [nums[i], nums[low], nums[high]]
                    current = abs(diff)

                if diff == 0:
                    return sum(res)
                elif diff > 0:
                    high -= 1
                elif diff < 0:
                    low += 1

        return sum(res)
