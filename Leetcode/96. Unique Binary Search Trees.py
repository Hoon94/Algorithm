class Solution:
    def numTrees(self, n: int) -> int:
        def countTrees(n):
            if n == 0:
                return 1
            if n == 1:
                return 1

            Result = 0

            for i in range(n):
                LeftTrees = countTrees(i)
                RightTrees = countTrees(n - i - 1)
                Result += LeftTrees * RightTrees

            return Result
