from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        r, record = set(), set()

        for i in range(len(s) - 9):
            substring = s[i:i+10]
            [record, r][substring in record].add(substring)

        return list(r)
