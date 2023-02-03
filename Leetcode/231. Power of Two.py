class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and sum(list(map(int, bin(n)[2:]))) == 1
