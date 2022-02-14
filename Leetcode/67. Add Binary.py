class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b, carry, ans = list(map(int, a)), list(map(int, b)), 0, []
        while a or b or carry:
            carry, res = divmod((a.pop() if a else 0) +
                                (b.pop() if b else 0) + carry, 2)
            ans.append(str(res))

        return ''.join(ans[::-1])
