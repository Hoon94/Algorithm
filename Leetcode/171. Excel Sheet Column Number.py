class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0

        for char, i in zip(columnTitle, range(len(columnTitle), 0, -1)):
            result += 26 ** (i - 1) * (ord(char) - 64)

        return result
