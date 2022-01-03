from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        l = len(candidates)

        stack = [([], 0, 0)]
        res = []

        while stack:
            comb, till, pos = stack.pop()
            if till == target:
                res.append(comb)
                continue
            if pos < l:
                i = pos
                prev = None
                while i < l:
                    if candidates[i] != prev and till + candidates[i] <= target:
                        stack.append(
                            (comb + [candidates[i]], till + candidates[i], i + 1))
                        prev = candidates[i]
                    i += 1

        return res
