class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        long = list()

        for char in s:
            if char in long:
                answer = max(answer, len(long))
                long = long[long.index(char) + 1:]
                long.append(char)
            else:
                long.append(char)
                
        answer = max(answer, len(long))
        
        return answer