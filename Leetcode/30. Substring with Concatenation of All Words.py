class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ret = []
        able = list(itertools.permutations(words, len(words)))
        # print(able)
        pairs = set([''.join(x) for x in able])
        # print(pairs)

        for pair in pairs:
            indice = s.find(pair)
            if indice != -1:
                ret.append(indice)

        return ret
