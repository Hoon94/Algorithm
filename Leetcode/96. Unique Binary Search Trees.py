class Solution:
    def numTrees(self, n: int) -> int:
        cache = {}

        def countTrees(n, cache):
            if n == 0:
                return 1
            if n == 1:
                return 1

            if cache.get(n, -1) != -1:
                return cache[n]

            Result = 0

            for i in range(n):
                LeftTrees = countTrees(i, cache)
                RightTrees = countTrees(n - i - 1, cache)
                Result += LeftTrees * RightTrees

            cache[n] = Result

            return Result

        return countTrees(n, cache)
