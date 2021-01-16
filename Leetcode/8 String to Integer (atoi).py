class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        sign = 1
        digit = [str(i) for i in range(10)]
        
        # 1 condition
        s = s.strip()
        
        for i, char in enumerate(s):
            # 2 condition
            if char == '-' and i + 1 < len(s) and s[i + 1] in digit:
                sign = -1
                print(char, sign)
            
            # 3 condition
            if char in digit:
                pass
        
        
        
        return res