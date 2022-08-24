from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one, two = 0, 0

        for x in nums:
            one, two, three = one ^ x, two | (one & x), two & x
            one, two = one & ~three, two & ~three

        return one
