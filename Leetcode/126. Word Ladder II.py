import string
from typing import List
import collections


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        tree, words, n = collections.defaultdict(
            set), set(wordList), len(beginWord)

        if endWord not in wordList:
            return []

        found, q, nq = False, {beginWord}, set()

        while q and not found:
            words -= set(q)
            for x in q:
                for y in [x[:i] + c + x[i + 1:] for i in range(n) for c in string.ascii_lowercase]:
                    if y in words:
                        if y == endWord:
                            found = True
                        else:
                            nq.add(y)

                        tree[x].add(y)

            q, nq = nq, set()

        def bt(x):
            return [[x]] if x == endWord else [[x] + rest for y in tree[x] for rest in bt(y)]

        return bt(beginWord)
