class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """[summary]
            Implement strStr().
            Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

            Clarification:
            What should we return when needle is an empty string? This is a great question to ask during an interview.
            For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

        Args:
            haystack (str): 0 <= haystack.length
            needle (str): needle.length <= 5 * 104

        Returns:
            int: Return the index

        Result:
            Runtime: 20 ms, faster than 99.24% of Python3 online submissions for Implement strStr().
            Memory Usage: 14.5 MB, less than 19.75% of Python3 online submissions for Implement strStr().
        """

        ret = haystack.find(needle)

        return ret
