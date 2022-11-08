from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        count = 0
        start = 0

        while count < len(nums):
            current = start
            prev = nums[start]

            while True:
                next = (current + k) % len(nums)
                temp = nums[next]
                nums[next] = prev
                prev = temp
                current = next
                count += 1

                if start == current:
                    break

            start += 1
