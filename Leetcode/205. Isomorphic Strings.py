class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return map(s.find, s) == map(t.find, t)
