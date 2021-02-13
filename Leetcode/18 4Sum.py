class Solution:
    def fourSum(self, nums: list, target: int) -> list:
        """[summary]
            Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target?
            Find all unique quadruplets in the array which gives the sum of target.

        Args:
            nums (List[int]): 0 <= nums.length <= 200, -109 <= nums[i] <= 109
            target (int): -109 <= target <= 109

        Returns:
            List[List[int]]: the solution set must not contain duplicate quadruplets.

        Result:
            Runtime: 1620 ms, faster than 12.13% of Python3 online submissions for 4Sum.
            Memory Usage: 14.5 MB, less than 32.48% of Python3 online submissions for 4Sum.
        """

        ret = set()
        nums.sort()
        n = len(nums)

        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                low = j + 1
                high = n - 1

                while low < high:
                    guess = (nums[i], nums[j], nums[low], nums[high])
                    guess_sum = sum(guess)

                    if target == guess_sum:
                        ret.add(guess)

                        while low < high and nums[low] == nums[low + 1]:
                            low += 1
                        while low < high and nums[high] == nums[high - 1]:
                            high -= 1

                        low += 1
                        high -= 1

                    elif target < guess_sum:
                        high -= 1
                    else:
                        low += 1

        return [list(r) for r in ret]
