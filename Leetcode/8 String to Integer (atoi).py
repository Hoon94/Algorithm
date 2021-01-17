class Solution:
    def myAtoi(self, s: str) -> int:
        res = '0'
        sign = 1
        maxres = 2 ** 31 - 1
        minres = -2 ** 31
        
        # 1 condition
        s = s.strip()
        
        if len(s) < 1:
            return 0
        
        # 2 condition
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        for char in s:                 
            # 3 condition
            if char.isdigit():
                res += char
            else:
                break
                
        res = int(res) * sign
        
        if minres <= res <= maxres:
            return res
        elif res < minres:
            return minres
        else:
            return maxres