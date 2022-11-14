import collections


class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = collections.Counter(bin(n)[2:])
        return counter.get("1", 0)
