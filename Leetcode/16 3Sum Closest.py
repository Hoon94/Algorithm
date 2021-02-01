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
        left, right = target, target

        unique = set(nums)

        while target != res:
            # target go right
            for i in range(len(nums) - 1):
                for j in range(i + 1, len(nums)):
                    if right - (nums[i] + nums[j]) in unique - set([nums[i], nums[j]]):
                        #print("1:{},{},{},{}".format(right - (nums[i] + nums[j]), nums[i], nums[j], right))
                        res = right

            right += 1

            # target go left
            for i in range(len(nums) - 1):
                for j in range(i + 1, len(nums)):
                    if left - (nums[i] + nums[j]) in unique - set([nums[i], nums[j]]):
                        #print("2 {}".format(left))
                        res = left

            left -= 1

        return res
