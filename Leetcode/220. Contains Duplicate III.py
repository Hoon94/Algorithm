from typing import List
from sortedcontainers import SortedSet


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if not nums or valueDiff < 0:
            return False

        ss, n = SortedSet(), 0

        for i, num in enumerate(nums):
            ceiling_idx = ss.bisect_left(num)
            floor_idx = ceiling_idx - 1

            if ceiling_idx < n and abs(ss[ceiling_idx] - num) <= valueDiff:
                return True

            if 0 <= floor_idx and abs(ss[floor_idx] - num) <= valueDiff:
                return True

            ss.add(num)
            n += 1

            if i - indexDiff >= 0:
                ss.remove(nums[i - indexDiff])
                n -= 1

        return False
