class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ''
        answer_len = 0
        
        for i in range(len(s)):
            # odd    
            left, right = i, i
            while 0 <= left and right < len(s) and s[left] == s[right]:
                if answer_len < right - left + 1:
                    answer = s[left : right + 1]
                    answer_len = right - left + 1
                left -= 1
                right += 1
                
            # even
            left, right = i, i + 1
            while 0 <= left and right < len(s) and s[left] == s[right]:
                if answer_len < right - left + 1:
                    answer = s[left : right + 1]
                    answer_len = right - left + 1
                left -= 1
                right += 1
                
        return answer