class Solution:
    def hammingWeight(self, n: int) -> int:
        num_of_1s = 0

        for _ in range(32):
            num_of_1s += (n & 1)
            n = n >> 1

        return num_of_1s
