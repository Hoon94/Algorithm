class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = [i.lower() for i in s if i.isalnum()]

        return newS[:len(newS) / 2] == newS[(len(newS) + 1) / 2:][::-1]
