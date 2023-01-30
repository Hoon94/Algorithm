from typing import List
import collections


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ctr = collections.Counter()

        for n in nums:
            ctr[n] += 1
            if len(ctr) == 3:
                ctr -= collections.Counter(set(ctr))

        return [n for n in ctr if nums.count(n) > len(nums) / 3]
