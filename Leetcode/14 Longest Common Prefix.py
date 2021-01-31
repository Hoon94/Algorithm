class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        """[summary]

        Args:
            strs (List[str]): words in a list

        Returns:
            str: return longest common prefix
        """

        result = ''

        strs = sorted(strs, key=lambda x: len(x))
        short = strs[0] if len(strs) > 0 else ''

        for i in range(len(short)):
            for word in strs:
                if short != word[:len(short)]:
                    short = short[:-1]
                    break
            else:
                result = short

            if len(result) > 0:
                break

        return result
