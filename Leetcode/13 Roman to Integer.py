class Solution:
    def romanToInt(self, s: str) -> int:
        rules = {"M": 1000, "D": 500, "C": 100,
                 "L": 50, "X": 10, "V": 5, "I": 1}
        res = rules[s[len(s) - 1]]

        for i in range(len(s) - 2, -1, -1):
            if rules[s[i]] < rules[s[i + 1]]:
                res -= rules[s[i]]
            else:
                res += rules[s[i]]

        return res
