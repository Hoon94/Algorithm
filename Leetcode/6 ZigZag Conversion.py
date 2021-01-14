class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = []
        array = [[] for i in range(numRows)]
        
        pattern = [i for i in range(numRows)] + [i for i in range(numRows - 2, 0, -1)]
        num = len(s) // len(pattern) + 1
        pattern = pattern * num
                
        for i, j in enumerate(s):
            array[pattern[i]].append(j)
            
        for i in range(numRows):
            res += array[i]
        
        return ''.join(res)