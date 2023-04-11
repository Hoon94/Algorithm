from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        N = len(nums) - 1
        nbits = N.bit_length()
        ans = 0

        for p in range(nbits):
            mask = 1 << p
            a = sum(1 if num & mask else 0 for num in nums)
            b = sum(1 if num & mask else 0 for num in range(1, N + 1))

            if a > b:
                ans |= mask

        return ans
