import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pattern = re.compile(f'{p}')

        result = pattern.match(s).group() if pattern.match(s) else None

        if s == result:
            return True
        else:
            return False
