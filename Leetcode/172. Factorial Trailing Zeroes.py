class Solution:
    def trailingZeroes(self, n: int) -> int:
        r = 0

        while n > 0:
            n /= 5
            r += n

        return r
