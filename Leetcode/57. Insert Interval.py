from typing import List
import heapq


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        heap, ans, = [], []

        for s, e in intervals + [newInterval]:
            heapq.heappush(heap, (s, -1))
            heapq.heappush(heap, (e, 1))

        cur, s = 0, None

        while heap:
            i, val = heapq.heappop(heap)

            if s is None:
                s = i

            cur += val

            if not cur:
                ans.append([s, i])
                s = None

        return ans
