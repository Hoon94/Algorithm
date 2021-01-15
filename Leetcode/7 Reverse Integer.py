class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        minx = -2 ** 31
        maxx = 2 ** 31 - 1
        
        if x >= 0:
            res = int(str(x)[::-1])
        else:
            res = -int(str(x)[:0:-1])
            
        if minx <= res <= maxx:
            return res
        else:
            return 0