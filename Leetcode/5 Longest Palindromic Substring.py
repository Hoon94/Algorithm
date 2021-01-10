class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ''
        
        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                word = s[i:j]
                if word == word[::-1] and len(word) > len(answer):
                    #print(word)
                    answer = word

        return answer