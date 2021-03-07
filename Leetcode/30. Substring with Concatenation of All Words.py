from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """[summary]
            You are given a string s and an array of strings words of the same length.
            Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.
            You can return the answer in any order.

        Args:
            s (str): 1 <= s.length <= 10 ** 4, s consists of lower-case English letters.
            words (List[str]): 1 <= words.length <= 5000, 1 <= words[i].length <= 30, words[i] consists of lower-case English letters.

        Returns:
            List[int]: Return all starting indices of substring(s)

        Result:
            Runtime: 60 ms, faster than 97.46% of Python3 online submissions for Substring with Concatenation of All Words.
            Memory Usage: 14.5 MB, less than 82.78% of Python3 online submissions for Substring with Concatenation of All Words.
        """

        if len(words) == 0:
            return []

        # initialize words_dict, l, ans
        l = len(words[0])
        words_dict = {}
        ans = []

        for word in words:
            words_dict[word] = words_dict.get(word, 0) + 1

        # sliding window(s)
        for k in range(l):
            left = k
            subd = {}
            count = 0
            for j in range(k, len(s) - l + 1, l):
                tword = s[j:j + l]
                # valid word
                if tword in words_dict:
                    subd[tword] = subd.get(tword, 0) + 1
                    count += 1
                    while subd[tword] > words_dict[tword]:
                        subd[s[left:left + l]] -= 1
                        left += l
                        count -= 1
                    if count == len(words):
                        ans.append(left)
                # not valid
                else:
                    left = j + l
                    subd = {}
                    count = 0

        return ans
