class Solution:
    phone = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl',
                6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}

    def letterCombinations(self, digits: str) -> list:
        """[summary]
            Given a string containing digits from 2-9 inclusive,
            return all possible letter combinations that the number could represent.
            Return the answer in any order.
            A mapping of digit to letters (just like on the telephone buttons) is given below.
            Note that 1 does not map to any letters.

        Args:
            digits (str): 0 <= digits.length <= 4, digits[i] is a digit in the range ['2', '9'].

        Returns:
            List[str]: all possible letter combinations

        Result:
            Runtime: 24 ms, faster than 96.27% of Python3 online submissions for Letter Combinations of a Phone Number.
            Memory Usage: 14.4 MB, less than 36.22% of Python3 online submissions for Letter Combinations of a Phone Number.
        """

        if not digits:
            return []

        res = []
        stack = [(0, "")]

        while stack:
            i, combo = stack.pop()
            if i == len(digits):
                res.append(combo)
            else:
                nextDigit = int(digits[i])
                letters = self.phone[nextDigit]

                for letter in letters:
                    stack.append((i + 1, combo + letter))

        return res
