class Solution:
    def intToRoman(self, num: int) -> str:
        """[summary]

        Args:
            num (int): 1 <= num <= 3999

        Returns:
            str: Roman numeral
        """

        rules = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90,
                 "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}

        res = ""
        for sym, val in rules.items():
            while num >= val:
                num -= val
                res += sym

        return res
