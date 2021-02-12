class Solution:
    def generateParenthesis(self, n: int) -> list:
        ret = []
        pair = ""
        parenthesis = ["(", ")"]

        def dfs(pair, n):
            for i in range(n):
                if pair[-1] == "(":
                    pair += ")"
                    pair = dfs(pair, n)
                else:
                    pair += "("
                    pair = dfs(pair, n - 1)

            return pair

        for i in range(n):
            pair = "("
            print(pair)
            print(type(pair))
            ret.append(dfs(pair, n - 1))

        return ret
