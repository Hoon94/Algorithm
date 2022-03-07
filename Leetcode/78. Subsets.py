from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        res = self.subsets(nums[:-1])

        for i in range(len(res)):
            res.append(res[i] + [nums[-1]])

        return res
