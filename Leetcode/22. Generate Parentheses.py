class Solution:
    def generateParenthesis(self, n: int) -> list:
        """[summary]
            Given n pairs of parentheses,
            write a function to generate all combinations of well-formed parentheses.

        Args:
            n (int): 1 <= n <= 8

        Returns:
            List[str]: all combinations of well-formed parentheses.

        Result:
            Runtime: 32 ms, faster than 86.32% of Python3 online submissions for Generate Parentheses.
            Memory Usage: 14.7 MB, less than 40.91% of Python3 online submissions for Generate Parentheses.
        """

        def dfs(ret, pair, openp, closep, maxp):
            if len(pair) == 2 * maxp:
                ret.append(pair)

            if openp < maxp:
                dfs(ret, pair + "(", openp + 1, closep, maxp)
            if closep < openp:
                dfs(ret, pair + ")", openp, closep + 1, maxp)

        ret = []
        pair = ""
        openp, closep = 0, 0

        dfs(ret, pair, openp, closep, n)

        return ret


"""
backtracking과 recursion 비교.
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.recursive(n, n, [], [])


    def recursive(self, o, c, curr, acc):
        if o == c and o == 0:
            acc.append("".join(curr))
            return acc
        
        if o > 0:
            curr.append("(")
            self.recursive(o - 1, c, curr, acc)
            curr.pop()
        if c > o:
            curr.append(")")
            self.recursive(o, c - 1, curr, acc)
            curr.pop()
        
        return acc
"""


if __name__ == "__main__":
    solution = Solution()
    print(solution.generateParenthesis(3))
