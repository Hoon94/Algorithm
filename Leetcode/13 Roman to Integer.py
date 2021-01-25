class Solution:
    rules = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

    def romanToInt(self, s: str) -> int:
        """[summary]

        Args:
            s (str): Roman number

        Returns:
            int: change Roman number to decimal
        """

        res = self.rules[s[-1]]

        for i in range(len(s) - 1):
            if self.rules[s[i]] < self.rules[s[i + 1]]:
                res -= self.rules[s[i]]
            else:
                res += self.rules[s[i]]

        return res
