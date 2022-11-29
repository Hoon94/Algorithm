class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1, d2 = [[] for _ in range(256)], [[] for _ in range(256)]

        for i, val in enumerate(s):
            d1[ord(val)].append(i)

        for i, val in enumerate(t):
            d2[ord(val)].append(i)

        return sorted(d1) == sorted(d2)
