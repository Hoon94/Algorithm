from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            pos, cur = i, nums[i]

            while pos > 0 and not self.compare(nums[pos - 1], cur):
                nums[pos] = nums[pos - 1]
                pos -= 1

            nums[pos] = cur

        return str(int("".join(map(str, nums))))

    def compare(self, n1, n2):
        return str(n1) + str(n2) > str(n2) + str(n1)
