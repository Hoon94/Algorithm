class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """[summary]
        Given a string containing just the characters '(' and ')',
        find the length of the longest valid (well-formed) parentheses substring.

        Args:
            s (str): 0 <= s.length <= 3 * 104, s[i] is '(', or ')'.

        Returns:
            int: length of the longest valid parentheses substring.

        Result:
            Runtime: 44 ms, faster than 72.77% of Python3 online submissions for Longest Valid Parentheses.
            Memory Usage: 14.7 MB, less than 50.18% of Python3 online submissions for Longest Valid Parentheses.
        """

        dp = [0 for x in range(len(s))]
        max_to_now = 0

        for i in range(1, len(s)):
            if s[i] == ')':
                # case 1: ()()
                if s[i - 1] == '(':
                    # add nearest parentheses pairs + 2
                    dp[i] = dp[i - 2] + 2
                # case 2: (())
                # i - dp[i - 1] - 1 is the index of last "(" not paired until this ")"
                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    if dp[i - 1] > 0:  # content within current matching pair is valid
                        # add nearest parentheses pairs + 2 + parentheses before last "("
                        dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                    else:
                        # otherwise is 0
                        dp[i] = 0
                max_to_now = max(max_to_now, dp[i])
        return max_to_now
