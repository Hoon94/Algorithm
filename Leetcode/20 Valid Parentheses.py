class Solution:
    def isValid(self, s: str) -> bool:
        """[summary]
            Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
            determine if the input string is valid.
            An input string is valid if:
                1. Open brackets must be closed by the same type of brackets.
                2. Open brackets must be closed in the correct order.

        Args:
            s (str): 1 <= s.length <= 104, s consists of parentheses only '()[]{}'.

        Returns:
            bool: Ture or False.

        Result:
            Runtime: 48 ms, faster than 10.17% of Python3 online submissions for Valid Parentheses.
            Memory Usage: 14.1 MB, less than 88.53% of Python3 online submissions for Valid Parentheses.
        """

        open = {"(": ")", "[": "]", "{": "}"}

        stack = []
        for s_ in s:
            if s_ in open:
                stack.append(s_)
            else:
                if len(stack) == 0:
                    return False
                if s_ is open[stack[-1]]:
                    del stack[-1]
                else:
                    return False

        if len(stack) > 0:
            return False
        else:
            return True
