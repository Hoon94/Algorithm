class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = self.helper(version1), self.helper(version2)

        return 1 if v1 > v2 else (-1 if v1 < v2 else 0)

    def helper(self, v):
        v = map(int, v.split("."))
        i = len(v) - 1

        while i >= 0 and v[i] == 0:
            i -= 1

        return v[:i+1]
